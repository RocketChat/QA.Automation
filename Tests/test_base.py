import pytest


@pytest.mark.usefixtures("init_driver")
@pytest.mark.usefixtures("init_driver_class")
class BaseTest:
    pass
