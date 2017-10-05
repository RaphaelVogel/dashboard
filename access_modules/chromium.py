from chromote import Chromote


def open_url(url):
    chrome = Chromote()
    tab = chrome.tabs[0]
    tab.set_url(url)
