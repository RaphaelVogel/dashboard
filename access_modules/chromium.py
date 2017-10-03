import pychrome

browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()


def open_url(url):
    tab.start()
    tab.Network.enable()
    tab.Page.navigate(url="https://github.com/fate0/pychrome", _timeout=8)
    tab.wait(8)
    tab.stop()