#!/usr/bin/env python

"""
Module for getting image informations from the folder that contains
all food images extracted from yelp.com.
"""

import os
import re
import glob
import yelpapi
from geopy import geocoders
from itertools import imap

IMAGES_SOURCE = '../static/images/foods'

def _listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))

def _get_geoinfo(address):
    """
    Get latitude and longitude informations from the given address.
    """
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(address)
    return lat, lng

def businesses_info(directory):
    """
    Find all detail business informations.

    Parameters
    ----------
    directory: folders that contains all businesses' food image. Each
               folder's name is a unique yelp business id.

    Returns
    -------
    A business informations dictionary.
    """
    business_info_dict = {}
    for subdir in _listdir_nohidden(directory):
        id = os.path.basename(subdir)
        yelp_info = yelpapi.find_business_by_id(id)
        business_info = {'name': yelp_info['name'],
                         'rating': yelp_info['rating'],
                         'phone': yelp_info['phone'],
                         'review_count': yelp_info['review_count'],
                         'category': yelp_info['categories']}
        location = {'display_name':
                        yelp_info['location']['display_address']}
        lat, lng = _get_geoinfo(", ".join(location['display_name']))
        location['details'] = {'latitude': lat, 'longitude': lng}
        business_info['location'] = location
        business_info_dict[id] = business_info
    return business_info_dict

def images_iter(directory):
    """
    Get a iterator that contains instances of jpg file info dict.

    Parameters
    ----------
    directory: full path of a directory

    Returns
    -------
    A iterator of a list of file info dictionary.
    (e.g: {'abspath': 'absolute path of the target file',
           'relpath': 'relative path of the target file',
           'description': 'description of the image',
           'businessid': 'yelp business id'})
    """

    def _imagefiles():
        "Get all of image files from given directory."
        for subdir in _listdir_nohidden(directory):
            subdir_path = os.path.join(os.path.abspath(directory), subdir)
            for f in _listdir_nohidden(subdir_path):
                yield os.path.join(os.path.abspath(subdir_path), f)

    def _parse_attribute(filepath):
        "Get image attribute from the path of image file."
        abspath = filepath
        relpath = os.path.relpath(filepath, '../static')
        description = re.match(r'(.*)\.jpg',
                               os.path.basename(filepath)).group(1)
        businessid = re.match(r'.*/(.*)$',
                              os.path.dirname(filepath)).group(1)
        return [filepath, relpath, description, businessid]

    def _jpg_file_info(attrlist):
        """
        Function for storing jpeg file infos.
        """
        attrs = ["abspath", "relpath", "description", "businessid"]
        return dict(zip(attrs, attrlist))

    return (_jpg_file_info(_parse_attribute(f)) for f in _imagefiles())
