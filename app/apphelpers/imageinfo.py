#!/usr/bin/env python

"""
Module for getting image informations from the folder that contains
all food images extracted from yelp.com.
"""

import os
import re
import glob
from itertools import imap

IMAGES_SOURCE = '../static/images/foods'

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
    def _listdir_nohidden(path):
        return glob.glob(os.path.join(path, '*'))

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
