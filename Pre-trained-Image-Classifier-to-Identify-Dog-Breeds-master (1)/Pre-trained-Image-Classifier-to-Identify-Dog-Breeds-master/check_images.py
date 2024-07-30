#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
# Filename: check_images.py

from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # Measure total program runtime by collecting start time
    start_time = time()

    # Retrieve command line arguments
    in_arg = get_input_args()

    # Check command line arguments
    check_command_line_arguments(in_arg)

    # Create results dictionary with pet image labels
    results = get_pet_labels(in_arg.dir)

    # Verify creation of pet image labels
    check_creating_pet_image_labels(results)

    # Classify images and update results dictionary
    classify_images(in_arg.dir, results, in_arg.arch)

    # Verify image classification
    check_classifying_images(results)

    # Adjust results to determine correct classification as dog/not-a-dog
    adjust_results4_isadog(results, in_arg.dogfile)

    # Verify adjustment for is-a-dog classification
    check_classifying_labels_as_dogs(results)

    # Calculate statistics from results
    results_stats = calculates_results_stats(results)

    # Verify calculation of results statistics
    check_calculating_results(results, results_stats)

    # Print results, including summaries and any incorrect classifications
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Compute and print total elapsed runtime in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          f"{int(tot_time // 3600)}:{int((tot_time % 3600) // 60)}:"
          f"{int((tot_time % 3600) % 60)}")

# Run the program


if __name__ == "__main__":
    main()
