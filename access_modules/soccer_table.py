import requests
from bs4 import BeautifulSoup, NavigableString
from collections import OrderedDict

SOCCER_1_URL = "http://www.dfb.de/bundesliga/spieltagtabelle/"
SOCCER_2_URL = "http://www.dfb.de/2-bundesliga/spieltagtabelle/"


def get_table_data(liga):
    if liga == "1":
        resp = requests.get(SOCCER_1_URL, timeout=8)
    else:
        resp = requests.get(SOCCER_2_URL, timeout=8)
    if resp.status_code != 200:
        return "ERROR: Cannot connect to soccer url"

    soup = BeautifulSoup(resp.text, 'html.parser')
    tables = soup.find_all("table")
    # table[0] is 'Aktueller Spieltag', table[1] is 'Tabelle'
    return_table = []
    for tr in tables[1].tbody.children:
        if isinstance(tr, NavigableString):
            continue
        club = OrderedDict()
        idx = 1
        for td in tr.children:
            if isinstance(td, NavigableString):
                continue
            if idx == 1:
                club['rank'] = td.string
            elif idx == 2:
                club['image'] = td.img['src']
            elif idx == 3:
                club['name'] = td.span.string
            elif idx == 4:
                club['games'] = td.string
            elif idx == 5:
                club['won'] = td.string
            elif idx == 6:
                club['equal'] = td.string
            elif idx == 7:
                club['loose'] = td.string
            elif idx == 8:
                club['goals'] = td.string
            elif idx == 9:
                club['goal_diff'] = td.string
            elif idx == 10:
                club['points'] = td.string
            idx += 1

        return_table.append(club)

    return return_table


def get_match_data(liga):
    if liga == "1":
        resp = requests.get(SOCCER_1_URL, timeout=8)
    else:
        resp = requests.get(SOCCER_2_URL, timeout=8)
    if resp.status_code != 200:
        return "ERROR: Cannot connect to soccer url"

    soup = BeautifulSoup(resp.text, 'html.parser')
    tables = soup.find_all("table")
    # table[0] is 'Aktueller Spieltag', table[1] is 'Tabelle'
    return_table = []
    for tr in tables[0].tbody.children:
        if isinstance(tr, NavigableString):
            continue
        match = OrderedDict()
        idx = 1
        for td in tr.children:
            if isinstance(td, NavigableString):
                continue
            if idx == 1:
                date_string = ""
                for child in td.descendants:
                    if not isinstance(child, NavigableString):
                        continue
                    date_string += child.string + " "
                match['date'] = date_string
            elif idx == 2:
                match['home_team'] = td.a.string
            elif idx == 3:
                match['home_image'] = td.img['src']
            elif idx == 4:
                match['result'] = td.a.string
            elif idx == 5:
                match['guest_image'] = td.img['src']
            elif idx == 6:
                match['guest_team'] = td.a.string

            idx += 1

        return_table.append(match)

    return return_table
