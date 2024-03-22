import os
import aiofiles
import aiohttp
import asyncio


async def upload():
    url = os.environ.get("apiUploadURL", None)
    password = os.environ.get("apiUploadPASS", None)

    async with aiofiles.open("paper-versions.json", "rb") as f:
        file_content = await f.read()

    data = aiohttp.FormData()
    data.add_field(
        "file",
        file_content,
        filename="paper-versions.json",
        content_type="application/json",
    )
    data.add_field("password", password)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            print(resp.status)
            print(await resp.text())
            return


if __name__ == "__main__":
    try:
        asyncio.run(upload())
    except Exception as E:
        print(E)
