import httpx
import asyncio
import time

base = "insert website url here"

client = httpx.AsyncClient(http2=True)
async def main():
    async with client:
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
        queue = []
        extentions = [".aspx"]
        chars = "ETAONRISHDLFCMUGYPWBVKJXQZetaonrishdlfcmugypwbvkjxqz0123456789_-$~"
        works = []
        for i in extentions:
            for j in chars:
                queue += [[j+"*~1*",i]]
        while len(queue) != 0:
            current = queue[0]
            #print(current)
            del queue[0]
            prefix = ""
            site = base + prefix + current[0] + "/" + current[1]
            response = await client.options(site, headers=headers)
            if response.status_code == 404:
                if len(current[0]) < 10:
                    for i in chars:
                        queue.insert(0,[current[0][0:len(current[0])-4] + i + "*~1*",current[1]])
                else:
                    works += [current]
            print(response, site)
            time.sleep(0.5)
        print(works)
asyncio.run(main())
