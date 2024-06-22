import tensorflow as tf
import numpy as np
import os
from glob import glob
from PIL import Image

def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def preprocess_image(image_path, target_size):
    image = Image.open(image_path)
    image = image.resize(target_size, Image.Resampling.NEAREST)
    image = image.convert('RGB')
    image = np.array(image).astype(np.uint8)
    return image

def load_test_data_with_labels(test_path, target_size, class_names):
    test_images = []
    test_labels = []
    for class_index, class_name in enumerate(class_names):
        class_folder_path = os.path.join(test_path, class_name)
        for image_path in glob(os.path.join(class_folder_path, '*.jpg')):
            image = preprocess_image(image_path, target_size)
            test_images.append(image)
            test_labels.append(class_index)  # Assign the index of the class name as the label
    return np.array(test_images), np.array(test_labels)

def evaluate_model(interpreter, test_data, test_labels):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    correct_predictions = 0
    for i, data in enumerate(test_data):
        data = np.expand_dims(data, axis=0)
        interpreter.set_tensor(input_details[0]['index'], data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        prediction = np.argmax(output_data[0])
        if prediction == test_labels[i]:
            correct_predictions += 1

    accuracy = correct_predictions / len(test_data)
    return accuracy

def main():
    model_path = r'C:\STM32\stm32ai-modelzoo\image_classification\src\experiments_outputs\MobileNetV2_7D\2024_03_31_17_38_52\quantized_models\quantized_model.tflite'
    test_data_path = r'C:\ImageClassification\Deployment3\Model1\image_classification\scripts\training\datasets\SERIOUS\Experiment 4\Final_Test'
    target_size = (128,128)
    class_names = ['Bacterial_Blight', 'Bacterial_Leaf_Streak', 'Dead_Heart', 'normal', 'Blast', 'Brownspot', 'Tungro']
    #[Bacterial_Blight, Blast, Brownspot, Tungro]
    #['Bacterial_Blight', 'Bacterial_Leaf_Streak', 'Bacterial_Panicle_Blight', 'Dead_Heart', 'Downy_Mildew', 'Hispa', 'normal', 'Blast', 'Brownspot', 'Tungro']

    print("Loading model...")
    interpreter = load_tflite_model(model_path)

    print("Loading test data...")
    test_data, test_labels = load_test_data_with_labels(test_data_path, target_size, class_names)
    print(f"Loaded {len(test_data)} images for testing.")

    print("Evaluating model...")
    accuracy = evaluate_model(interpreter, test_data, test_labels)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
