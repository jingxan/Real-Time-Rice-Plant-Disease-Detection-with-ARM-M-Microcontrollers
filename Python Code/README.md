# Python Code
## Data Augmentation
To use the data_augmentation.py script, first open the script and input the folder path for your dataset. It's recommended to use the same folder so that the newly created images are kept in the same location as the original images. If you prefer to keep the augmented images separate, you will need to copy the original images to the augmented_data_dir folder. Additionally, you can specify the number of images for a certain class if you don’t want that class to follow the default value.

## Evaluate Model Accuracy
To evaluate model accuracy using the test_tf_model.py script, input the model path of your .tflite model and then input the folder that contains all the test images in the test_data_path. Remember to update the target size, which corresponds to your model's input size, and also specify the class names accordingly.

## Create Test Dataset
This script, create_test_dataset.py, is designed to create a test dataset from your original dataset by randomly selecting a specified number of images from each class in your dataset and moving them to a separate test directory.
