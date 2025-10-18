from pathlib import Path
import random
import time
import requests
import more_itertools


def is_parent(parent, child):
    return Path(parent).resolve() in Path(child).resolve().parents


def main():
    print("Welcome to qBittorrent random cleaner interactive script!")

    print("Firstly, we need to test qBittorrent connection")
    port = input(
        "\nPlease enter webui port (can be found at qBittorrent - Tools - Options - WebUI):\n"
    )
    port = int(port)

    print("testing...")

    qb_url = f"http://localhost:{port}"

    # get all completed torrents
    response = requests.get(
        f"{qb_url}/api/v2/torrents/info",
        params={
            "filter": "completed",
        },
    )

    if not response.ok:
        raise Exception(
            f"qBittorrent webui api get torrents info failed. response status: {response.status_code}, response text: {response.text}"
        )

    torrents = response.json()
    print(f"successfully get completed torrents: {len(torrents)}")

    # user select directory
    dir_to_clean = input("\nPlease enter directory to clean (e.g. D://Download):\n")

    torrents = [p for p in torrents if is_parent(dir_to_clean, p["content_path"])]

    print(f"Directory {dir_to_clean} torrents count: {len(torrents)}")

    # download complete time filter
    complete_day_threshold_str = input(
        "\nPlease enter complete_day_threshold (unit: days) (default 30):\n"
    )

    complete_day_threshold = 30
    if complete_day_threshold_str:
        complete_day_threshold = int(complete_day_threshold_str)

    torrents = [
        p
        for p in torrents
        if p["completion_on"] < int(time.time()) - complete_day_threshold * 86400
    ]

    print(
        f"After filter {complete_day_threshold} days, torrents count: {len(torrents)}"
    )

    # randomly remove
    delete_probability_str = input(
        "\nPlease enter delete_probability (0-1) (default 0.3):\n"
    )

    delete_probability = 0.3
    if delete_probability_str:
        delete_probability = float(delete_probability_str)

    delete_count = int(len(torrents) * delete_probability)

    # sort torrents randomly
    random.shuffle(torrents)

    torrents = torrents[:delete_count]

    # list them from new to old
    torrents.sort(key=lambda p: p["completion_on"], reverse=True)

    print(f"Torrents selected for removal: {len(torrents)}.")
    input("\nType enter to show selected torrents")

    for i, p in enumerate(torrents):
        print(f"{i+1}: {p['content_path']}")

    # confirm
    confirm = input("\nAre you sure to remove these torrents? (type Y to confirm)\n")
    if confirm != "Y":
        print("Aborted.")
        return

    # remove
    batch_size = 10
    batches = list(more_itertools.chunked(torrents, batch_size))

    print(f"removing. batch_size={batch_size}, batches={len(batches)}")

    for i, batch in enumerate(batches):
        hashes = "|".join([p["hash"] for p in batch])
        print(f"batch {i+1}/{len(batches)}, hashes: {hashes}")

        response = requests.post(
            f"{qb_url}/api/v2/torrents/delete",
            data={
                "hashes": hashes,
                "deleteFiles": True,
            },
        )

        if not response.ok:
            raise Exception(
                f"qBittorrent webui api delete torrents failed. response status: {response.status_code}, response text: {response.text}"
            )

    print("done")


if __name__ == "__main__":
    main()
