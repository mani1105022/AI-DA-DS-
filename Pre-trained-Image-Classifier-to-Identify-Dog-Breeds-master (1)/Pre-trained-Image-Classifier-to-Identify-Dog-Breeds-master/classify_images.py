#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.


def classify_images(images_dir, results_dic, model):
    """
    This function uses a classifier function to classify images and compares
    the classifier labels to the actual pet labels. The results, including
    classifier labels and a comparison flag, are added to the results dictionary.

    Parameters:
      images_dir - The full path to the folder of images that are to be classified
                   by the classifier function (string)
      results_dic - Dictionary with 'key' as image filename and 'value' as a list.
                    The list contains:
                      index 0 = pet image label (string)
                    This function adds:
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int), 1 = match between pet image and classifier labels, 0 = no match
      model - The CNN model architecture to be used by the classifier function to
              classify the pet images. Options are: 'resnet', 'alexnet', 'vgg' (string)

    Returns:
      None - results_dic is mutable, so no return is needed.
    """
    for image_file in results_dic:
        # Get the full path to the image file
        img_path = images_dir + "/" + image_file

        # Use the classifier function to get the classifier label
        classifier_label = classifier(img_path, model).lower().strip()

        # Get the real label from the results dictionary
        real_label = results_dic[image_file][0]

        # Determine if the real label matches the classifier label
        match = 1 if real_label in classifier_label else 0

        # Add the classifier label and match result to the results dictionary
        results_dic[image_file].extend([classifier_label, match])

    return None
