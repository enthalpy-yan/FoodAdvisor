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

####1. Install virtualenv, npm, bower
####2. Under the root directory, Install a virtual environment using install.sh (or install.bat for Windows):
    $ ./install.sh
####3. Activate the corresponding environment. do the following:
    $ source flask/bin/activate
####4. Now, when you check you python path, it should be like this:
    $ which python
    /Users/hanyan/Desktop/Homework/CS598/FoodAdvisor/flask/bin/python
####5. Run the service(under the root directory):
    $ python run.py


##Folder Structure
    FoodAdvisor/
        ├── app
        │   ├── helpers           (All self-created functions)
        │   ├── imagesearchapis   (Implements image search apis)
        │   ├── restapis          (Implements RESTful apis )
        │   ├── routes            (App routes)
        │   └── static            (Front-end Angular App)
        ├── flask                 (Flask virtual environment)
        ├── node_modules          (Node dependencies)
