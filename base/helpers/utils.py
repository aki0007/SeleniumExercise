from collections.abc import MutableSequence
from datetime import datetime
from typing import Union

MySequenceType = Union[MutableSequence, tuple, set]


def calculate_number_of_clicks(date_obi: datetime) -> int:
    today: datetime = datetime.now()
    number_of_clicks: int = (today.year - date_obi.year) * 12 + (
        today.month - date_obi.month
    )
    return number_of_clicks

