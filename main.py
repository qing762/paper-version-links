import aiohttp
import json
import asyncio
import sys
import os


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            paperData = {}
            versions = []
            async with session.get(
                "https://fill.papermc.io/v3/projects/paper",
                headers={"accept": "application/json"},
            ) as response:
                response = await response.json()
                for major, minor in response["versions"].items():
                    versions.extend(minor)
                paperData["latest"] = versions[0]
                data = {}
                for x in versions:
                    async with session.get(
                        f"https://fill.papermc.io/v3/projects/paper/versions/{x}",
                        headers={"accept": "application/json"},
                    ) as response:
                        response = await response.json()
                        versionName = response["version"]["id"]
                        latestBuildNumber = response["builds"][0]
                        buildReq = await session.get(
                            f"https://fill.papermc.io/v3/projects/paper/versions/{x}/builds/{latestBuildNumber}",
                            headers={"accept": "application/json"},
                        )
                        res = await buildReq.json()
                        data[versionName] = res["downloads"]["server:default"]["url"]
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
