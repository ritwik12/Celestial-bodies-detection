import pytest


def pytest_addoption(parser):
    """ Adds parser for pytest testing """
    parser.addoption("--image_dir", action="store", default="./training_data")


@pytest.fixture(scope='session')
def image_dir(request):
    dir_val = request.config.option.image_dir
    if dir_val is None:
        pytest.fail()
    return dir_val
