#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results from the program run using the classifier's model
    architecture to classify pet images. The function then stores the statistics in a
    dictionary (results_stats_dic) which is returned for printing, helping the user
    determine the 'best' model for classifying images. The statistics calculated
    are either percentages or counts.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List:
                    index 0 = pet image label (string)
                    index 1 = classifier label (string)
                    index 2 = 1/0 (int)  where 1 = match between pet image and
                            classifier labels and 0 = no match between labels
                    index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet image 'is-NOT-a' dog.
                    index 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                         a percentage or a count) where the key is the statistic's
                         name (starting with 'pct' for percentage or 'n' for count)
                         and the value is the statistic's value.
    """
    results_stats_dic = {
        'n_images': 0,
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }

    # Count total images
    results_stats_dic['n_images'] = len(results_dic)

    # Process through results_dic to calculate the counts
    for key in results_dic:
        # Number of label matches
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Check if pet image label is a dog
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            # Check if classifier label is a dog
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

            # Check if pet image label and classifier label match (correct breed)
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        else:
            # Check if pet image label is not a dog
            results_stats_dic['n_notdogs_img'] += 1

            # Check if classifier label is not a dog
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100

    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic[
            'n_dogs_img']) * 100
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic[
            'n_dogs_img']) * 100
    else:
        results_stats_dic['pct_correct_dogs'] = 0
        results_stats_dic['pct_correct_breed'] = 0

    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic[
            'n_notdogs_img']) * 100
    else:
        results_stats_dic['pct_correct_notdogs'] = 0

    return results_stats_dic
