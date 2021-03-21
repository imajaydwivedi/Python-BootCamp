import asyncio

async def main():
    print('hello')
    await asyncio.sleep(5)
    print('world')

asyncio.run(main())
