# example of usage of asynchronous programming in Python (asyncio library)
import asyncio

# async  will make function a coroutine
async def count():
    print("One")
    # await will pass control back to the event loop
    # execution of count will be suspended until the result is returned
    await asyncio.sleep(1)
    print("Two")

async def mygen(bound = 20):
    """Yield power of number 2"""
    i = 0
    while i < bound:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)
