#FoodAdvisor

FoodAdvisor is a simple food image search app that helps people to find where
to eat with the given food image. It is also a Final Project for CS598 Visual
Information Retrieval in Stevens Institute of Technology.

##Artechiture

In this project, We use Flask framework to create a RESTful service that serves the data for our Front-end rich client application written by AngularJS. Since we chose JSON as our API format, we chose MongoDB as our JSON data store.

##Features

We created a image based food search service hoping to find the most similar foods. We have used Yelp API to provide a location based business information. The features of the app are as follows: 

- Search food image with the given image file.
- Search food image with the given text: picture description, location or business name.
- Filter result by alphabetic, location and rating.

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

  1. Install virtualenv, npm, bower

  2. Under the root directory, Install a virtual environment using install.sh (or install.bat for Windows)
     
    `$ ./install.sh`
  3. Activate the corresponding environment. do the following
    
    `$ source flask/bin/activate`
  4. Now, when you check your python path, it should be like this
        
    ```
    $ which python
    /Users/hanyan/Desktop/Homework/CS598/FoodAdvisor/flask/bin/python
    ```
  5. Run the service(under the root directory), the server should be running without any issues.
    `$ python run.py`

####Data

  - Run preparedata.py script under app/dbhelpers/ to insert data into database(Make sure your local mongodb server is openning).
  
    ```
    $ cd app/dbhelpers
    $ python preparedata.py
    ```

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
query(optional) | filter result by location
sortbylocation(optional) | filter result by rating
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
