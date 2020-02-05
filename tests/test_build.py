import pytest
from hub.examples.image_retraining.retrain import *

# Main test function
def test_class_count_value(image_dir):
    testing_percentage = 10
    validation_percentage = 10
    list_of_images = create_image_lists(None.image_dir, testing_percentage, validation_percentage)
    count_value = len(list_of_images.keys())
    assert count_value > 1