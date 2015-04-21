import requests
from bs4 import BeautifulSoup, NavigableString

EBAY_KLEINANZEIGEN = "http://kleinanzeigen.ebay.de/anzeigen/s-74909/l8136"


def get_data():
    resp = requests.get(EBAY_KLEINANZEIGEN)
    if resp.status_code != 200:
        return "ERROR: Cannot connect to ebay kleinanzeigen"

    soup = BeautifulSoup(resp.text)
    sections = soup.find_all("section")
    return_data = []
    for section in sections:
        if isinstance(section, NavigableString):
            continue
        if section.get('class') and section['class'][0] == "ad-listitem-image":
            if section.a.get('data-imgsrc'):
                entry = {'image_url': section.a['data-imgsrc']}
            else:
                entry = {'image_url': '/lib/images/nopic.png'}
        elif section.get('class') and section['class'][0] == "ad-listitem-main":
            entry['text'] = section.h2.a.string
        elif section.get('class') and section['class'][0] == "ad-listitem-details":
            entry['price'] = section.strong.string
            return_data.append(entry)

    return return_data