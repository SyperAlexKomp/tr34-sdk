import asyncio

from tr34_sdk import TR34Api

api = TR34Api(key="sdfds")

async def get_posts_test():
    assert await api.search_posts(tags=['ass'], limit=10)

async def main():
    await get_posts_test()

if __name__ == "__main__":
    asyncio.run(main())

