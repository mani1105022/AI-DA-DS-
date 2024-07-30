#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. 
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Generates a dictionary of pet labels based on the filenames of the image files.
    These labels are used to verify the accuracy of the labels returned by the classifier.
    Filenames contain the true identity of the pet in the image.

    Parameters:
     image_dir - The full path to the folder containing pet images (string).

    Returns:
      results_dic - Dictionary where each key is an image filename, and each value is a list containing:
        index 0 = pet image label (string), formatted as lowercase with leading and trailing whitespace removed.
    """
    # List all files in the specified directory
    filenames = listdir(image_dir)

    # Create an empty dictionary to hold results
    results_dic = {}

    # Process each file in the directory
    for filename in filenames:
        if not filename.startswith('.'):
            # Extract the pet label from the filename
            words = filename.lower().split('_')
            pet_label = ' '.join(word for word in words if word.isalpha()).strip()

            # Add the filename and pet label to the dictionary
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print(
                    f'\nWARNING: The file "{filename}" is already in results_dic with value = "{results_dic[filename]}"')

    # Print the results for verification
    print('\nKey-value pairs in results_dic:')
    for key, value in results_dic.items():
        print(f'Filename = {key:>25}    Pet label = {value[0]}')

    # Return the dictionary with the results
    return results_dic
