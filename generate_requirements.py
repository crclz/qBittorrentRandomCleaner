import tomllib

# tomllib: python 3.11 support

with open('pyproject.toml', 'rb') as f:
    pyproject_data = tomllib.load(f)

dependencies = pyproject_data['project']['dependencies']

# 写入requirements.txt文件
with open('requirements.txt', 'w') as f:
    for dep in dependencies:
        f.write(f"{dep}\n")

    