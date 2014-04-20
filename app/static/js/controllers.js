'use strict';

/* Controllers */

angular.module('foodAdvisor.controllers', [])
  .controller('SearchController',
             function ($scope, $http, $location, cfpLoadingBar, geolocation) {
    $scope.currentValue = '';
    $scope.imageData = null;
    $scope.originalData = null;
    $scope.distance = 0;
    $scope.lat = 0;
    $scope.lng = 0;
    $scope.queryString = null;
    $scope.offset = 24;

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
      $http({method: 'GET', url: 'api/foodimages/search?query=' + query['title']}).
        success(function(data, status, headers, config) {
          $scope.originalData = data;
          $scope.imageData = $scope.originalData['result'];
        }).
        error(function(data, status, headers, config) {
      });
    };

    $scope.$watch('queryString', function(value) {
      if (value != null) {
        $scope.offset = 24;
        $http({method: 'GET', url: 'api/foodimages/search?query=' + value['title']}).
          success(function(data, status, headers, config) {
            $scope.originalData = data;
            $scope.imageData = $scope.originalData['result'];
          }).
          error(function(data, status, headers, config) {
        });
      }
    });

    $scope.clickSort = function(sortMethod) {
      switch(sortMethod) {
        case 0:
          $scope.imageData =
            _.sortBy($scope.imageData,
                     function(data) {return data['description']});
          break;
        case 1:
          var sorted =
            _.sortBy($scope.imageData,
                     function(data) {return data['description']});
          $scope.imageData = sorted.reverse();
          break;
        case 2:
          var sorted =
            _.sortBy($scope.imageData,
                     function(data) {return data['business_info']['rating']});
          $scope.imageData = sorted.reverse();
          break;
        case 3:
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

    $scope.getData = function() {
      $http({method: 'GET', url: '/test'}).
      success(function(data, status, headers, config) {
        $scope.originalData = data;
        $scope.imageData = $scope.originalData['result'];
      }).
      error(function(data, status, headers, config) {
      });
    };

    $scope.nextPage = function() {
      if ($scope.originalData.status.file != null)
        $http({method: 'GET',
              url: 'api/foodimages/search?file=' +
                    $scope.originalData.status.file +
                    '&offset=' + $scope.offset})
          .success(function(data, status, headers, config) {
            $scope.originalData = data;
            console.log($scope.originalData);
            $scope.imageData = $scope.originalData['result'];
            $scope.offset += 12
          }).
          error(function(data, status, headers, config) {
        });
      else {
        $http({method: 'GET',
              url: 'api/foodimages/search?query=' +
                    $scope.originalData.status.text +
                    '&offset=' + $scope.offset})
          .success(function(data, status, headers, config) {
            $scope.originalData = data;
            $scope.imageData = $scope.originalData['result'];
            $scope.offset += 12
          }).
          error(function(data, status, headers, config) {
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
      $scope.imageData[index]['dist'] = _.parseInt(d);
      return d.toFixed(2);
    };

      $scope.items = ['item1', 'item2', 'item3'];

    $scope.open = function (index) {
      $location.path("/business");
    };
  })
  .controller('ModalInstanceCtrl', function ($scope) {
    $scope.$on('viewState.viewEnter', function(e, d) {
      var mapEl = angular.element(document.querySelector('.angular-google-map'));
      var iScope = mapEl.isolateScope();
      var map = iScope.map;
      google.maps.event.trigger(map, "resize");
    });

    $scope.map = {
        center: {
            latitude: 45,
            longitude: -73
        },
        zoom: 8
    };
  });

//Helper functions
function toRad(Value) {
    /** Converts numeric degrees to radians */
    return Value * Math.PI / 180;
}
