#!/usr/bin/env python

"""
Script for prepare data for FoodAdvisor
"""

from imageinfo import images_info

IMAGES_SOURCE = '../static/images/foods'
BUSINESSES_DATA_DES = '../outputs/business_data.txt'
IMAGES_DATA_DES = '../outputs/images_data.txt'

if __name__ == '__main__':
    images_info(IMAGES_SOURCE, BUSINESSES_DATA_DES, IMAGES_DATA_DES)

