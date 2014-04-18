'use strict';

/* Controllers */

angular.module('foodAdvisor.controllers', []).
  controller('AppCtrl', function ($scope) {
  }).
  controller('searchBarController',
             function ($scope, $http, cfpLoadingBar, geolocation) {
    $scope.currentValue = '';
    $scope.imageData = null;
    //Geo location initialization
    $scope.coords = geolocation.getLocation().then(function(data){
        return {lat: data.coords.latitude,
                long: data.coords.longitude};
    });
    $scope.submitText = function() {
      console.log($scope.keywords);
    };
    $scope.receiveFromPost = function(data, status) {
      cfpLoadingBar.complete();
      console.log(data);
    };
    $scope.getData = function() {
      $http({method: 'GET', url: '/test'}).
      success(function(data, status, headers, config) {
          console.log(data)
          $scope.imageData = data
      }).
      error(function(data, status, headers, config) {
      });
    }
  });
