import sys
import aiohttp
import subprocess
import json
import asyncio
import os

if len(sys.argv) < 2:
    print("Please provide a file name as a command-line argument.")
    sys.exit(1)


async def lintCheck():
    print("Checking format and style...")
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--select=E9,F63,F7,F82",
                "--show-source",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed with {str(e)}")
        sys.exit(1)
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--max-complexity=15",
                "--max-line-length=300",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed with {str(e)}")
        sys.exit(1)
    print("Linting passed!\n\n")


async def validateLinks():
    print("Validating links...")
    file = sys.argv[1]

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)

    urls = [url for url in data["versions"].values()]

    all_links_valid = True
    invalidURL = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                if response.status == 200:
                    print("0")
                else:
                    print(f"Link is invalid: {url}")
                    all_links_valid = False
                    invalidURL.append(url)

    if all_links_valid:
        print("All links are valid!\n\n")
    else:
        print(f"Invalid links found:\n{invalidURL}\n\n")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(lintCheck())
        asyncio.run(validateLinks())
        print("All check passed!")
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
