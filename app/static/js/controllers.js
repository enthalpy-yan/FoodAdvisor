'use strict';

/* Controllers */

angular.module('foodAdvisor.controllers', []).
  controller('AppCtrl', function ($scope) {
  }).
  controller('searchBarController', function ($scope) {
    $scope.people = [{'name': 'aaa'}, {'name': 'bbb'}, {'name': 'ccc'}];
  });
