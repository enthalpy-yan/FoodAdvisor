'use strict';

/* Directives */
angular.module('foodAdvisor.directives', [])
  .directive('uploadButton', ['$parse', '$compile', 'cfpLoadingBar', function($parse, $compile, cfpLoadingBar){
    return {
      restrict: 'E',
      replace: true,
      transclude: true,
      template: btnTemplate(),
      link: function(scope, element, attrs) {
        element.find('input').bind('change', function() {
          var fd = new FormData();
          // send to server as uploadFile field
          fd.append('uploadFile', this.files[0]);
          // create xhr
          var xhr = new XMLHttpRequest();
          xhr.addEventListener("load", function(e) {
            var fn = $parse(attrs.complete);
            scope.$apply(function () {
              if(fn) { fn(scope, { $data: xhr.responseText, $status: xhr.status }); }
            });
          }, false);
          xhr.open("POST", attrs.action);
          xhr.send(fd);
          cfpLoadingBar.start();
        });
      }
    };
  }])
  .directive('ngEnter', [function() {
    return function(scope, element, attrs) {
      element.bind("keydown keypress", function(event) {
        if(event.which === 13) {
          scope.$apply(function(){
            scope.$eval(attrs.ngEnter, {'event': event});
          });

          event.preventDefault();
        }
      });
    };
  }]);

// directive template
function btnTemplate() {
  return '<span class="{{class}}" style="position: relative;overflow: hidden;margin-right: 4px;"' +'>' +
           '<span ng-transclude></span>' +
           '<input type="file" style="width:50px; position: absolute;top: 0;right: 0;margin: 0;opacity: 0;filter: alpha(opacity=0);transform: translate(-300px, 0) scale(4);font-size: 23px;direction: ltr;cursor: pointer;">' +
         '</span>';
}

