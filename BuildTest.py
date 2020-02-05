import pytest
from hub.examples.image_retraining.retrain import create_image_lists


class BuildTest:
    def up_and_run(self):
        pass
    
    def class_count_value(self, image_dir):
        testing_percentage = 10
        validation_percentage = 10

        list_of_images = create_image_lists(self.image_dir, testing_percentage, validation_percentage)
        count_value = len(list_of_images.keys())
        assert count_value > 1
    
    


