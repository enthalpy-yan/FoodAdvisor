#FoodAdvisor

FoodAdvisor is a simple food image search app that helps people to find where
to eat with the given food image. It is also a Final Project for CS598 Visual
Information Retrieval in Stevens Institute of Technology.

##Artechiture

In this project, We use Flask framework to create a RESTful service that serves the data for our Front-end rich client application written by AngularJS. Since we chose JSON as our API format, we chose MongoDB as our JSON data store.

##Technology Stacks

###Back-end

API Server: [Flask 0.10.1](http://flask.pocoo.org/)

Persistence: [MongoDB 2.6](https://www.mongodb.org/)

Image Search: [OpenCV-Python](http://docs.opencv.org/trunk/doc/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html#py-table-of-content-setup), [Scipy Library](http://www.scipy.org/scipylib/index.html), [Numpy](http://www.numpy.org)

Data source: [Yelp](http://www.yelp.com)(food images), [Yelp API](http://api.yelp.com)(business info)

###Front-end

App: [AngularJS](http://angularjs.org/), [Lo-Dash](http://lodash.com/), [Grunt](http://gruntjs.com/)

Style: [Bootstrap](http://getbootstrap.com/), [LESS](http://lesscss.org/), [FontAwesome](http://fortawesome.github.io/Font-Awesome/)

##Development

###Folder Structure
    FoodAdvisor/
        ├── app
        │   ├── apphelpers        (Self-created global use functions)
        │   ├── dbhelpers         (Self-created db-related functions)
        │   ├── imagesearchapis   (Implements image search apis)
        │   ├── restapis          (Implements RESTful apis )
        │   ├── routes            (App routes)
        │   └── static            (Front-end Angular App)
        │   └── outputs           (folder for saving output files)
        ├── flask                 (Flask virtual environment)
        ├── node_modules          (Node dependencies)

###Configuration
####Environment

  1. Install Python, MongoDB, OpenCV-Python.

  2. Under the root directory, install python dependencies.

    `$ ./installtolocal.sh`

  3. Run the service(under the root directory), the server should be running without any issues.

    `$ python run.py`
  
  Note: If there is an error about nltk, try to install it manually as follow:
    
    `$ python -m nltk.downloader stopwords`

####Data

  - Run preparedata.py script under app/dbhelpers/ to insert data into database(Make sure your local mongodb server is openning).

    ```
    $ cd app/dbhelpers
    $ python preparedata.py
    ```

####To Do List

#####Image Searching Algorithm:

- Collect images 
- Extract SIFT features from all the images and save them to SIFT pool
- Cluster all SIFT features
- Re-represent each image with bag of words
- Calculate tf-idf for all images
- Do inverted file indexing
- Accept incoming image as query
- Return highest rank images

#####Back-end server:

- Text suggestion search from the field including ‘description’, ‘category’, ‘name’. 
- Full text search from the field including ‘description’, ‘category’, ‘name’.
- REST API for searching food image with the given image file.
- REST API for Search food image with the given text: picture description, location or business name.


#####Front-end:

- A Flat, minimal looking interface.
- Single page. 
- Text searching bar with autocomplete support.
- Upload file through XHR.
- Single upload file button with automatic submit.
- Menu button for sorting result.
- Load more button for pagination.
- Progress bar for any long wait operation.
- Animations for better user experience.

###RESTful Service
####Text autocomplete
Resource                   |      Method
:------------------------- |-----------:|
/api/foodtext/search &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| GET

Parameter                  |Description
:------------------------- |-----------:|
term &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| keyword strings or prefixes

####food image/text search
Resource                   |      Method
:------------------------- |-----------:|
/api/foodimages/search &nbsp;    | GET/POST
Resource:

Parameter                  |Description
:------------------------- |-----------:|
longitude(optional) | client longitude information
latitude(optional) | client latitude information
offset(optional) | Offset the list of returned image results by this amount
query(optional) | text query
sortbylocation(optional) | filter result by location
sortbyrating(optional) | filter result by rating
sortbyname(optional) | filter result by alphabetic

###DB document sample
    {
        "description": "Amazing chicken tikka and aloo tacos",
        "abspath": "/Users/hanyan/Desktop/Homework/CS598/FoodAdvisor/app/static/images/foods/23rd-street-cafe-los-angeles/Amazing chicken tikka and aloo tacos.jpg",
        "business_id": "23rd-street-cafe-los-angeles",
        "image_id": 0,
        "relpath": "images/foods/23rd-street-cafe-los-angeles/Amazing chicken tikka and aloo tacos.jpg",
        "business_info": {
            "category": [
                [
                    "Indian",
                    "indpak"
                ],
                [
                    "Mexican",
                    "mexican"
                ],
                [
                    "American (New)",
                    "newamerican"
                ]
            ],
            "rating": 4.0,
            "review_count": 178,
            "name": "23rd Street Cafe",
            "phone": "+1-213-749-1593",
            "location": {
                "display_name": [
                    "936 W 23rd St",
                    "University Park",
                    "Los Angeles, CA 90007"
                ],
    			"details" : {
    				"type" : "Point",
    				"coordinates" : [
    					-118.2808464,
    					34.033785
    				]
    			}
            }
        }
    }
###Result sample
    {
        "result": [...],
        "status": {"text": last text query, "file": the file name(server side) of the last image query}
    }
