import requests
import pprint as pp

#  @TODO add items into a dictionary [x]

from all_content import AllContent

page_content = requests.get("http://drurybuildings.com/menus/").content
page = AllContent(page_content)

menu_items = page.item

for item in menu_items:  # @FIXME items won't allow string operations [X]
    print(str(item).strip('<p>').strip('</p>'))




