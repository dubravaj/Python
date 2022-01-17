import logging
import re
from typing import IO, List, Pattern, Set
import asyncio
from aiohttp import ClientSession, ClientError
from aiohttp.http_exceptions import HttpProcessingError
import aiofiles

logging.basicConfig(format="%(levelname)s:%(name)s: %(message)s", level=logging.DEBUG)


class Scrapper:
    """Example of using asynchronous libraries"""

    def __init__(self, filename, outfile):
        self.urls_file = filename
        self.output_file = outfile
        self.logger = logging.getLogger("asynclogger")
        self.pattern = re.compile(r'href="(.*?)"')

    def load_urls(self):
        """Load urls from file"""
        with open(self.urls_file, "r") as urls_file:
            self.urls = set(map(str.strip, urls_file))

    async def fetch_url_content(self, url: str, session: ClientSession):
        """Fetch content of the url"""
        response = await session.request("GET", url=url)
        response.raise_for_status()
        self.logger.info("URL [%s] response: %s", url, response.status)
        content = await response.text()
        return content

    async def find_pattern(self, pattern: Pattern[str], content: str) -> Set[str]:
        """Find all matches for given pattern"""
        pattern_occurences = pattern.findall(content)
        return set(pattern_occurences)

    async def scrap_and_write(self, url: str, session: ClientSession) -> None:
        """Scrap the links of the webpage and write it to the file"""
        try:
            content = await self.fetch_url_content(url=url, session=session)
        except (ClientError, HttpProcessingError) as e:
            self.logger.error(f"Unable to get content for url: {url}")
            return None
        else:
            occurences = await self.find_pattern(self.pattern, content)
            if not occurences:
                return None
            async with aiofiles.open(self.output_file, "a") as f:
                for occurence_str in occurences:
                    await f.write(f"{url}\t{occurence_str}\n")
                self.logger.info(f"Writing pattern match results for url: {url}")

    async def scrap(self):
        """Scrap url content"""
        self.load_urls()
        async with ClientSession() as session:
            scrap_tasks = []
            for url in self.urls:
                scrap_tasks.append(self.scrap_and_write(url, session))
            await asyncio.gather(*scrap_tasks)
