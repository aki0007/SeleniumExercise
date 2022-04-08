from typing import Any, Optional

import requests
from requests import Response

from base.data import login_data
from config import config


def login_request(url: str = None, data: dict = None) -> None:
    # Api login request
    url = url if url else config.GLOBAL_URL + config.TESTING_URL
    data = data if data else login_data
    body_template: Optional[dict[Any, Any]] = {
        "_hidCheckSubmit": 2,
        "_txtUserName": data["username"],
        "_txtPassword": data["password"],
    }
    r: Response = requests.post(url=url, data=body_template)

    assert r.status_code == 200
