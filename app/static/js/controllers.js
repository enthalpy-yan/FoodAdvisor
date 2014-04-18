'use strict';

/* Controllers */

angular.module('foodAdvisor.controllers', []).
  controller('AppCtrl', function ($scope) {
  }).
  controller('searchBarController', function ($scope) {
    $scope.currentValue = '';
    $scope.submitText = function() {
        console.log($scope.keywords);
    };
  });
