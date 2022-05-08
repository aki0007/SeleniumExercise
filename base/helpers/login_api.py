from typing import Any, Optional

import requests
from requests import Response

from base.data import LOGIN_DATA
from config import conf_obj


def login_request(url: str = None, data: dict = None) -> None:
    # Api login request
    url: str = url if url else conf_obj.GLOBAL_URL + conf_obj.TESTING_URL
    data: dict = data if data else LOGIN_DATA
    body_template: Optional[dict[Any, Any]] = {
        "_hidCheckSubmit": 2,
        "_txtUserName": data["username"],
        "_txtPassword": data["password"],
    }
    r: Response = requests.post(url=url, data=body_template)

    assert r.status_code == 200
