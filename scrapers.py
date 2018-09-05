from lxml import html
import requests

def search_scrape(url, inputs=[], xpath, li=-1):

    if not inputs == []:
        page = requests.get(url.format(inputs[0]))
    else:
        page = requests.get(url)

    tree = html.fromstring(page.content)

    if li > -1:
        output = tree.xpath(xpath)[li]
    else:
        output = tree.xpath(xpath)

    return output
