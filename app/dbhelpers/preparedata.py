#!/usr/bin/env python

"""
Script for inserting data into database.
"""

from inserthelper import insert_images

if __name__ == '__main__':
    insert_images('../outputs/images_data.txt', 'FoodAdvisor', 'images')
