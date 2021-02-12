import pytest
from Config.data_open import OpenData
from Config.data_local import LocalData


class Data:
    def __init__(self):
        self.env = "Local"

    def get_data(self):
        if self.env == "Local":
            return LocalData()
        else:
            return OpenData()
