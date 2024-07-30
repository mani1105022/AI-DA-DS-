#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
# Filename: print_results.py

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Summarizes and displays the results of the image classification process,
    including detailed statistics and optional reports on misclassified dogs
    and incorrect dog breeds if requested.

    Parameters:
      results_dic - A dictionary where each key is an image filename and each
                    value is a list containing:
                      index 0: Actual pet label (string)
                      index 1: Classifier label (string)
                      index 2: Binary flag (1/0) indicating if the labels match
                      index 3: Binary flag (1/0) indicating if the actual label is a dog
                      index 4: Binary flag (1/0) indicating if the classifier identified it as a dog
      results_stats_dic - A dictionary with statistical measures, where the keys are:
                           - 'n_images': Total number of images
                           - 'n_dogs_img': Number of dog images
                           - 'n_notdogs_img': Number of non-dog images
                           - 'pct_correct_dogs': Percentage of correctly identified dog images
                           - 'pct_correct_notdogs': Percentage of correctly identified non-dog images
                           - 'pct_correct_breed': Percentage of correctly identified dog breeds
      model - String indicating the CNN model architecture used for classification (values: 'resnet', 'alexnet', 'vgg')
      print_incorrect_dogs - Boolean flag to indicate if incorrectly classified dog images should be printed
      print_incorrect_breed - Boolean flag to indicate if incorrectly classified dog breeds should be printed

    Returns:
      None - Outputs results to the console.
    """
    # Print the model used
    print(f'\nModel: {model}')

    # Print statistics on the number of images and the counts of dog and non-dog images
    print(f'\nTotal Images: {results_stats_dic["n_images"]} \nNumber of Dog Images: {results_stats_dic["n_dogs_img"]} \nNumber of "Not-a" Dog Images: {results_stats_dic["n_notdogs_img"]}')

    # Print all statistics from the results_stats_dic dictionary
    for stat_key, stat_value in results_stats_dic.items():
        if stat_key.startswith('pct'):
            print(f'{stat_key}: {stat_value}')

    # Print incorrectly classified dogs if requested
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print('\nIncorrectly Classified Dogs:')
        for filename, labels in results_dic.items():
            if sum(labels[3:]) == 1:  # Indicates incorrect classification of a dog
                print(f'\nPet Label: {labels[0]} \nClassifier Label: {labels[1]}')

    # Print incorrectly classified breeds if requested
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print('\nIncorrectly Classified Breeds:')
        for filename, labels in results_dic.items():
            if sum(labels[3:]) == 2 and labels[2] == 0:  # Indicates incorrect breed classification
                print(f'\nPet Label: {labels[0]} \nClassifier Label: {labels[1]}')
