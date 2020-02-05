import pytest

def pytest_addoption(parser):
    parser.addoption("--image_dir", action="store", default="training_data")

@pytest.fixture(scope='session')
def image_dir(request):
    dir_val = request.config.option.image_dir
    return dir_val