import pytest
from hub.examples.image_retraining.retrain import *

class BuildTest:
    def test_one(self):
        x = 'neural'
        assert "e" in x