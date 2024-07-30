#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER:  MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024             <=(Date Revised - if any)
# PURPOSE:  This set of functions can be used to check your code after programming 
#           each function. The top section of each part of the lab contains
#           the section labeled 'Checking your code'. When directed within this
#           section of the lab one can use these functions to more easily check 
#           your code. See the docstrings below each function for details on how
#           to use the function within your code.
#
##

# Functions below defined to help with "Checking your code", specifically
# running these functions with the appropriate input arguments within the
# main() funtion will print out what's needed for "Checking your code"


def check_command_line_arguments(in_arg):
    """
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each of the command line arguments provided as parameter in_arg.
    Assumes you have defined the three command line arguments as outlined in
    '7. Command Line Arguments'.

    Parameters:
     in_arg - Data structure storing the command line arguments object.

    Returns:
     None - Prints to console.
    """
    if in_arg is None:
        print("* Command Line Arguments not checked: 'get_input_args' function is missing.")
    else:
        # Print command line arguments
        print(
            f"Command Line Arguments:\n     dir = {in_arg.dir}\n    arch = {in_arg.arch}\n dogfile = {in_arg.dogfile}")


def check_creating_pet_image_labels(results_dic):
    """
    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Prints the first 10 key-value pairs and ensures there are 40 key-value
    pairs in the results_dic dictionary.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)

    Returns:
     None - Prints to console.
    """
    if results_dic is None:
        print("* Results Dictionary not checked: 'get_pet_labels' function is missing.")
    else:
        # Print the count of key-value pairs
        total_pairs = len(results_dic)
        print(f"\nPet Image Label Dictionary contains {total_pairs} key-value pairs.")

        # Determine how many pairs to print
        num_to_print = min(total_pairs, 10)
        print(f"Displaying {num_to_print} of them:")

        # Print first 10 or fewer key-value pairs
        for index, (key, value) in enumerate(results_dic.items()):
            if index < num_to_print:
                print(f"{index + 1:2d} key: {key:>30}  label: {value[0]:>26}")


def check_classifying_images(results_dic):
    """
    For Lab: Classifying Images - 11/12. Classifying Images
    Prints Pet Image Label and Classifier Label for all matches followed by all
    non-matches. Also prints total images, matches, and non-matches.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int) where 1 = match between pet image and classifier labels,
                                          0 = no match

    Returns:
     None - Prints to console.
    """
    if results_dic is None:
        print("* Results Dictionary not checked: 'classify_images' function is missing.")
    elif len(next(iter(results_dic.values()))) < 2:
        print("* Results Dictionary not checked: 'classify_images' function is missing.")
    else:
        # Initialize counters
        n_match = 0
        n_not_match = 0

        # Print matches
        print("\n     MATCH:")
        for key, value in results_dic.items():
            if value[2] == 1:
                n_match += 1
                print(f"\n{key:>30}:\nReal: {value[0]:>26}   Classifier: {value[1]:>30}")

        # Print non-matches
        print("\n NOT A MATCH:")
        for key, value in results_dic.items():
            if value[2] == 0:
                n_not_match += 1
                print(f"\n{key:>30}:\nReal: {value[0]:>26}   Classifier: {value[1]:>30}")

        # Print totals
        print(f"\n# Total Images: {n_match + n_not_match}, # Matches: {n_match}, # Not Matches: {n_not_match}")


def check_classifying_labels_as_dogs(results_dic):
    """
    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Prints Pet Image Label, Classifier Label, whether the Pet Label is a dog (1=Yes, 0=No),
    and whether the Classifier Label is a dog (1=Yes, 0=No) for all matches followed by all non-matches.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int) where 1 = match, 0 = no match
                    idx 3 = 1/0 (int) where 1 = pet image is a dog, 0 = not a dog
                    idx 4 = 1/0 (int) where 1 = classifier classifies image as a dog, 0 = not a dog

    Returns:
     None - Prints to console.
    """
    if results_dic is None:
        print("* Results Dictionary not checked: 'adjust_results4_isadog' function is missing.")
    elif len(next(iter(results_dic.values()))) < 4:
        print("* Results Dictionary not checked: 'adjust_results4_isadog' function is missing.")
    else:
        # Initialize counters
        n_match = 0
        n_not_match = 0

        # Print matches
        print("\n     MATCH:")
        for key, value in results_dic.items():
            if value[2] == 1:
                n_match += 1
                print(
                    f"\n{key:>30}:\nReal: {value[0]:>26}   Classifier: {value[1]:>30}  \nPetLabelDog: {value[3]:1d}  ClassLabelDog: {value[4]:1d}")

        # Print non-matches
        print("\n NOT A MATCH:")
        for key, value in results_dic.items():
            if value[2] == 0:
                n_not_match += 1
                print(
                    f"\n{key:>30}:\nReal: {value[0]:>26}   Classifier: {value[1]:>30}  \nPetLabelDog: {value[3]:1d}  ClassLabelDog: {value[4]:1d}")

        # Print totals
        print(f"\n# Total Images: {n_match + n_not_match}, # Matches: {n_match}, # Not Matches: {n_not_match}")


def check_calculating_results(results_dic, results_stats_dic):
    """
    For Lab: Classifying Images - 14. Calculating Results
    Prints statistics from the results_stats dictionary, then compares with
    the statistics calculated using the results dictionary.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int) where 1 = match, 0 = no match
                    idx 3 = 1/0 (int) where 1 = pet image is a dog, 0 = not a dog
                    idx 4 = 1/0 (int) where 1 = classifier classifies image as a dog, 0 = not a dog
     results_stats_dic - Dictionary with statistics where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.

    Returns:
     None - Prints to console.
    """
    if results_stats_dic is None:
        print("* Results Stats Dictionary not checked: 'calculates_results_stats' function is missing.")
    else:
        # Initialize counters and total number of images
        total_images = len(results_dic)
        count_pet_dogs = 0
        count_classified_dogs = 0
        count_classified_not_dogs = 0
        count_correct_breed_matches = 0

        # Compute statistics
        for value in results_dic.values():
            if value[2] == 1:
                if value[3] == 1:
                    count_pet_dogs += 1
                    if value[4] == 1:
                        count_classified_dogs += 1
                        count_correct_breed_matches += 1
                elif value[4] == 0:
                    count_classified_not_dogs += 1
            elif value[3] == 1:
                count_pet_dogs += 1
                if value[4] == 1:
                    count_classified_dogs += 1
            elif value[4] == 0:
                count_classified_not_dogs += 1

        count_pet_not_dogs = total_images - count_pet_dogs
        pct_correct_dog = (count_classified_dogs / count_pet_dogs) * 100 if count_pet_dogs > 0 else 0
        pct_correct_not_dog = (count_classified_not_dogs / count_pet_not_dogs) * 100 if count_pet_not_dogs > 0 else 0
        pct_correct_breed = (count_correct_breed_matches / count_pet_dogs) * 100 if count_pet_dogs > 0 else 0

        # Print statistics
        print
