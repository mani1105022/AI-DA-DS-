#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/test_classifier.py
#                                                                             
# PROGRAMMER: MANIAKNDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024         <=(Date Revised - if any)
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. See the example
#          usage below.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Imports classifier function for using pretrained CNN to classify images 
from classifier import classifier

# Define the path to a sample image within the pet_images folder
image_path = "pet_images/Collie_03797.jpg"

# Choose the CNN model architecture for image classification
# Available options: 'vgg', 'alexnet', 'resnet'
chosen_model = "vgg"

# Classify the sample image using the selected model
# The result is a string with image labels, which might include multiple
# descriptive terms separated by commas
classification_result = classifier(image_path, chosen_model)

# Display the classification outcome
print(f"\nResults from print_results.py\nImage Path: {image_path}\n"
      f"Model Used: {chosen_model}\nClassified As: {classification_result}")
