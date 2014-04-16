#FoodAdvisor

FoodAdvisor is a simple food image search app that helps people to find where
to eat with the given food image. It is also a Final Project for CS598 Visual
Information Retrieval in Stevens Institute of Technology.

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
  5. Run the service(under the root directory)
    `$ python run.py`

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
                "details": {
                    "latitude": 34.033785,
                    "longitude": -118.2808464
                }
            }
        }
    }
