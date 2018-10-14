__version__ = '0.1.0'

from mkdocs.plugins import BasePlugin
import os.path
import datetime


class Date(BasePlugin):
    def parse_url(self, url):
        try:
            pieces = url.split('/')
            year = int(pieces[0])
            month = int(pieces[1])
            day = int(pieces[2])
            return datetime.date(year, month, day)
        except ValueError:
            return None

    def xon_pre_page(self, page, files, config):
        d = self.parse_url(page.url)
        return page

    def on_page_markdown(self, markdown, page, files, config):
        d = self.parse_url(page.url)
        if d:
            page.title = d.strftime("%A, %B %d, %Y")
            page.meta['date'] = d
        return markdown
