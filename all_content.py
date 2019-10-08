from bs4 import BeautifulSoup

from drink_locator import DrinkLocators


class AllContent:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    def __repr__(self):
        return f'<{self.item}'

    @property
    def item(self):
        return self.soup.select(DrinkLocators.MENU_ITEM_LOCATOR)


