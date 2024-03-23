import asyncio

from tr34_sdk import TR34Api

api = TR34Api()

async def main():
    post_list = await api.search_random_posts(amount=10)
    for post in post_list:
        print(post.url)

if __name__ == "__main__":
    asyncio.run(main())

