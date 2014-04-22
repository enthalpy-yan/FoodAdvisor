angular.module('scrollto', []);

angular.module('scrollto')
  .directive('scrollTo', ['$timeout', function ($timeout) {

    return {
      restrict: 'A',
      link: function (scope, element, attrs) {
        element.on('click', function () {
          jQuery(element).scrollTop(0);
        });
      }
    };
  }]);
