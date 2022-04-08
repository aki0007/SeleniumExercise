from config import config
import requests
from base.data import login_data


def login_request(url=None, data=None):
    url = url if url else config.GLOBAL_URL + config.TESTING_URL
    data = data if data else login_data
    body_template = {'_hidCheckSubmit': 2,
                     '_txtUserName': data["username"],
                     '_txtPassword': data["password"]}
    r = requests.post(url=url, data=body_template)

    assert r.status_code == 200
