#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: MANIKANDAN K
# DATE CREATED: 25.07.2024
# REVISED DATE: 25.07.2024
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
import argparse


def get_input_args():
    """
    Parses and retrieves the command line arguments provided by the user when
    they execute the program from the terminal. This function utilizes Python's
    argparse module to define and handle three command line arguments. Default
    values are used if any of the arguments are not provided by the user.

    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'

    Returns:
      Namespace object containing the command line arguments
    """
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description='Process some images.')

    # Define command line arguments
    parser.add_argument('--dir', type=str, default='pet_images',
                        help='Path to the folder containing pet images')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture to use')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='Path to the text file with dog names')

    # Parse and return the command line arguments
    return parser.parse_args()
