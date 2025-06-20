import asyncio


async def a(x=3):
    for i in range(x):
        out = "a.x{}".format(i)
        print(out)
        await asyncio.sleep(1)


async def b(x=3):
    for i in range(x):
        out = "b.x{}".format(i)
        print(out)
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
tasks = [a(),b()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

