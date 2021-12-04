import logging
import asyncio
import aiohttp
from aiohttp import ClientSession
import aiofiles

logging.basicConfig(
    format="%(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG
)

class Scrapper:
    """Example of using asynchronous libraries"""
    
    def __init__(self, filename):
        self.urls_file = filename
        self.logger = logging.getLogger("aiologger")

    def load_urls(self):
        """Load urls from file"""
        with open(self.urls_file,"r") as urls_file:
            self.urls = set(map(str.strip, urls_file))

    async def fetch_url_content(self, url: str, session: ClientSession):
        """Fetch content of the url"""
        response = await session.request("GET", url=url)
        response.raise_for_status()
        self.logger.info("URL [%s] response: %s", url, response.status)
        content = await response.text()
        return content

    async def scrap(self):
        """Scrap url content"""
        self.load_urls()
        async with ClientSession() as session:
            for url in self.urls:
                content = await self.fetch_url_content(url=url,session=session)
                print(content)