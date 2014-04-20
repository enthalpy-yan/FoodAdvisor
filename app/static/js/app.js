'use strict';

angular.module('foodAdvisor', [
   //Self created dependencies
  'foodAdvisor.controllers',
  'foodAdvisor.services',
  'foodAdvisor.directives',
  'foodAdvisor.filters',

   //3rd party dependencies
  'ngResource',
  'ngAnimate',
  'ngRoute',
  'ui.bootstrap',
  'ui.date',
  'angucomplete',
  'chieffancypants.loadingBar',
  'geolocation'
]).
config(function ($routeProvider, $locationProvider) {
  $routeProvider.
    when('/', {
      templateUrl: 'views/home.html',
      controller: 'SearchController'
    }).
    when('/how', {
      templateUrl: 'views/how.html',
      controller: ''
    }).
    when('/about', {
      templateUrl: 'views/about.html',
      controller: ''
    }).
    otherwise({
      redirectTo: '/'
    });
  $locationProvider.html5Mode(true);
});
