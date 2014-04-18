'use strict';

/* Controllers */

angular.module('foodAdvisor.controllers', []).
  controller('AppCtrl', function ($scope) {
  }).
  controller('searchBarController', function ($scope, $http) {
    $scope.currentValue = '';
    $scope.imageData = null;
    $scope.submitText = function() {
        console.log($scope.keywords);
    };
    $scope.getData = function() {
        $http({method: 'GET', url: '/test'}).
        success(function(data, status, headers, config) {
            console.log(data)
            $scope.imageData = data
        }).
        error(function(data, status, headers, config) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
        });
    }
  });
