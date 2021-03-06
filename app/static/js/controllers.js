'use strict';

/* Controllers */

angular.module('foodAdvisor.controllers', [])
  .controller('SearchController',
             function ($scope, $http, $modal, $log, $location, cfpLoadingBar, geolocation, ImageService) {

    $scope.imageData = null;
    $scope.originalData = null;
    $scope.distance = 0;
    $scope.lat = 0;
    $scope.lng = 0;
    $scope.queryString = null;
    $scope.offset = 24;
    $scope.resultsByPressEnterInInputBar = null;
    $scope.sortMethod = null;

    //Geo location initialization
    $scope.getCurrentLocation = function() {
      geolocation.getLocation().then(function(data){
        $scope.lat = data.coords.latitude;
        $scope.lng = data.coords.longitude;
      });
    }

    $scope.submitText = function(query) {
      $scope.offset = 24;
      if (query == null)
        return;
      ImageService.getImages({'query': query['title']})
        .then(function(data) {
          $scope.originalData = data;
          $scope.imageData = $scope.originalData['result'];
        }, function(error) {

        });
    };

    $scope.$watch('resultsByPressEnterInInputBar',
                  function(newValue, oldValue) {
      if (newValue != null) {
        $scope.originalData = newValue;
        $scope.imageData = $scope.originalData['result'];
      }
    });

    $scope.$watch('queryString', function(value) {
      if (value != null) {
        $scope.offset = 24;
        ImageService.getImages({'query': value['title']})
          .then(function(data) {
            $scope.originalData = data;
            $scope.imageData = $scope.originalData['result'];
          }, function(error) {

          });
      }
    });

    $scope.clickSort = function(sortMethod) {
      sortResult(sortMethod);
    };

    var sortResult = function(sortMethod) {
      switch(sortMethod) {
        case 0:
          $scope.sortMethod = 0;
          $scope.imageData =
            _.sortBy($scope.imageData,
                     function(data) {return data['description']});
          break;
        case 1:
          $scope.sortMethod = 1;
          var sorted =
            _.sortBy($scope.imageData,
                     function(data) {return data['description']});
          $scope.imageData = sorted.reverse();
          break;
        case 2:
          $scope.sortMethod = 2;
          var sorted =
            _.sortBy($scope.imageData,
                     function(data) {return data['business_info']['rating']});
          $scope.imageData = sorted.reverse();
          break;
        case 3:
          $scope.sortMethod = 3;
          $scope.imageData =
            _.sortBy($scope.imageData,
                     function(data) {return data['dist']});
          break;
      }
    };

    //Callback function for receive data after post file to server.
    $scope.receiveFromPost = function(data, status) {
      cfpLoadingBar.complete();
      $scope.offset = 24;
      $scope.originalData = JSON.parse(data);
      $scope.imageData = $scope.originalData['result'];
    };

    $scope.nextPage = function() {
      if ($scope.originalData.status.file != null)
        ImageService.getImages({'file': $scope.originalData.status.file,
                                'offset': $scope.offset})
          .then(function(data) {
            $scope.originalData = data;
            $scope.imageData = $scope.originalData['result'];
            if ($scope.sortMethod != null) {
              sortResult($scope.sortMethod);
            };
            $scope.offset += 12
          }, function(error) {

          });
      else {
        ImageService.getImages({'query': $scope.originalData.status.text,
                                'offset': $scope.offset})
          .then(function(data) {
            $scope.originalData = data;
            $scope.imageData = $scope.originalData['result'];
            if ($scope.sortMethod != null) {
              sortResult($scope.sortMethod);
            };
            $scope.offset += 12
          }, function(error) {

          });
      }
    }

    //Function for set rating color with the given rating score.
    $scope.ratingColor = function(rating) {
      function setColor(color) {
        return {'background' : color};
      };
      if (rating >= 4) {
        return setColor('#27ae60');
      } else if (rating >=3 && rating < 4) {
          return setColor('#d35400');
      } else if (rating >=2 && rating < 3) {
          return setColor('#f39c12');
      } else {
          return setColor('#c0392b');
      }
    };

    //Function for calculate distance between two Geo location.
    $scope.getDistance = function(index, lat1, lon1, lat2, lon2) {
      //Helper functions
      function toRad(Value) {
          /** Converts numeric degrees to radians */
          return Value * Math.PI / 180;
      }

      //Radius of the earth in:  1.609344 miles,  6371 km  | var R = (6371 / 1.609344);
      var R = 3958.7558657440545; // Radius of earth in Miles
      var dLat = toRad(lat2-lat1);
      var dLon = toRad(lon2-lon1);
      var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
              Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
              Math.sin(dLon/2) * Math.sin(dLon/2);
      var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
      var d = R * c;

      if (d > 5000) {
        return null;
      }
      $scope.imageData[index]['dist'] = parseFloat(d);
      return d.toFixed(2);
    };

    $scope.open = function (index) {
      var modalInstance = $modal.open({
        templateUrl: 'views/mapmodal.html',
        controller: 'ModalInstanceCtrl',
        resolve: {
          businessinfo: function () {
            return $scope.imageData[index];
          }
        }
      });

      modalInstance.opened.then(function(){
      });
    };
  })
  .controller('ModalInstanceCtrl',
              function ($scope, $modalInstance, businessinfo) {
    $scope.business = businessinfo;

    $scope.map = {
        center: {
            latitude: businessinfo.business_info.location.details.coordinates[1],
            longitude: businessinfo.business_info.location.details.coordinates[0]
        },
        zoom: 15,
    };

    $scope.showMap = true;

    $scope.ok = function () {
      $modalInstance.close();
    };
  })
  .controller('AboutController', function($scope) {
    $scope.developers = [{'name': 'Han Yan',
                          'avatar': 'images/hy_avatar.jpg',
                          'roles': 'Architecture/Front-end/Back-end',
                          'dspt': 'As the architect of FoodAdvisor, Han leads our awesome team and is responsible for almost everything about our application.'},
                         {'name': 'MinHui Gu',
                          'avatar': 'images/mhg_avatar.jpg',
                          'roles': 'Back-end/Image Algorithms',
                          'dspt': 'Combining her image processing algorithm knowledges with development skill, MinHui designed and implemented bunch of algorithms related to image retrieval. She is the brains behind the technology of the food image search engine.'},
                         {'name': 'Lei Zhang',
                          'avatar': 'images/lz_avatar.jpg',
                          'roles': 'Back-end/DBM',
                          'dspt': 'Lei, a certified MongoDB developer who brings range of database management experiences to our team. He is also responsible for the design and implementation of our APIs.'},
                         {'name': 'YunJun Wang',
                          'avatar': 'images/yjw_avatar.jpg',
                          'roles': 'Front-end/Docs',
                          'dspt': 'As a beginner of Front-end development, YunJun always has strong passion to learn.'},
                         {'name': 'HaoPeng Men',
                          'avatar': 'images/hpm_avatar.jpg',
                          'roles': 'Back-end/API',
                          'dspt': 'HaoPeng is an experienced JAVA developer who helps us build the Back-end APIs using Python.'}];
  });
