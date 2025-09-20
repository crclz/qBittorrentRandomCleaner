import requests


def main():
    print("Welcome to qBittorrent random cleaner interactive script!")

    print("Firstly, we need to test qBittorrent connection")
    port = input("Please enter webui port (can be found at qBittorrent - Tools - Options - WebUI):\n")
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


if __name__ == "__main__":
    main()
