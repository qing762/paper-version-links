import aiohttp
import json
import asyncio
import sys
import os


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            paperData = {}
            async with session.get(
                "https://api.papermc.io/v2/projects/paper",
                headers={"accept": "application/json"},
            ) as response:
                response = await response.json()
                latestVersion = response["versions"][-1]
                paperData["latest"] = latestVersion
                data = {}
                for x in reversed(response["versions"]):
                    async with session.get(
                        f"https://api.papermc.io/v2/projects/paper/versions/{x}",
                        headers={"accept": "application/json"},
                    ) as response:
                        response = await response.json()
                        versionName = response["version"]
                        latestBuildNumber = response["builds"][-1]
                        latestBuildURL = f"https://api.papermc.io/v2/projects/paper/versions/{versionName}/builds/{latestBuildNumber}/downloads/paper-{versionName}-{latestBuildNumber}.jar"
                        data[versionName] = latestBuildURL
                paperData["versions"] = data
                return paperData


if __name__ == "__main__":
    try:
        data = asyncio.run(Main.main())
        with open("paper-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
