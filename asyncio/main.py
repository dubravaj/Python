from os import path
import pathlib
import asyncio
from asyncio_demo import count, mygen
from async_scrapper import Scrapper

async def main():
    await asyncio.gather(count(),count())
    powers = [num async for num in mygen(5)]
    print(powers)
    
    # scrapping demo
    file = pathlib.Path(__file__).parent.joinpath("urls.txt")
    scrapper = Scrapper(file)
    await scrapper.scrap()


if __name__ == "__main__":
    asyncio.run(main())