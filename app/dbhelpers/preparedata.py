#!/usr/bin/env python

"""
Script for inserting data into database.
"""

from inserthelper import insert_images
from updatehelper import update_collection, create_indexes

if __name__ == '__main__':
    insert_images('../outputs/images_data.txt', 'FoodAdvisor', 'images')
    update_collection('FoodAdvisor', 'images')
    create_indexes('test', 'images')
