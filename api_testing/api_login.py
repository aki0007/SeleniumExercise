import requests
from library.data import login_data
from config.config_reader import read_config_data


def login_request(url=None, data=None):
    url = url if url else read_config_data("Details", "URL")
    data = data if data else login_data
    body_template = {'_hidCheckSubmit': 2,
                     '_txtUserName': data["username"],
                     '_txtPassword': data["password"]}
    r = requests.post(url=url, data=body_template)

    assert r.status_code == 200

