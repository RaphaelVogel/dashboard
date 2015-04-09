import requests
from bs4 import BeautifulSoup, NavigableString

PIC_OF_DAY_URL = "http://www.spiegel.de/fotostrecke/augenblicke-bilder-des-tages-2015-fotostrecke-122824.html"


def get_pic_url():
    resp = requests.get(PIC_OF_DAY_URL, proxies={'http': 'http://proxy:8080'})
    if resp.status_code != 200:
        return "ERROR: Cannot connect to picture of the day url"

    soup = BeautifulSoup(resp.text)
    meta_tags = soup.find_all("meta")
    return_data = {}
    for meta_tag in meta_tags:
        if isinstance(meta_tag, NavigableString):
            continue
        if meta_tag.has_key('property') and meta_tag['property'] == "og:image":
            return_data['url'] = meta_tag['content']
        if meta_tag.has_key('property') and meta_tag['property'] == "og:description":
            return_data['text'] = meta_tag['content']

    return return_data