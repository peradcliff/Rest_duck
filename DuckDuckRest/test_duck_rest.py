import pytest
import requests

from DuckDuckRest.duck_rest import list_of_presidents

url_ddg = "https://api.duckduckgo.com"


def test_president_list():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    president_list = list_of_presidents()
    is_present = False

    for p in president_list:
        for last_name in rsp_data["RelatedTopics"]:
            if p in last_name["Text"]:
                is_present = True

    assert is_present
