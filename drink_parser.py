from drink_locator import DrinkLocators


class DrinkParser:
    """
    obj: take in a html page and scan specifically for drinks @TODO
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<{self.item}'

    @property
    def item(self):
        locator = DrinkLocators.MENU_ITEM_LOCATOR
        item_link = self.parent.select_all(locator)
        return item_link
