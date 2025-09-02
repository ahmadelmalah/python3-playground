import asyncio
async def my_coroutine() -> None:
    print('Hello, World!')

# You can'ty call it directly
my_coroutine()

# To call it
asyncio.run(my_coroutine())