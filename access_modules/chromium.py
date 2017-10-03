import pychrome

browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()
tab.start()
tab.Network.enable()


def open_url(newurl):
    tab.Page.navigate(url=newurl, _timeout=5)
    tab.wait(5)