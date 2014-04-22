'use strict';

/* Services */

angular.module('foodAdvisor.services', []).
    factory('ImageService', function($http, $q) {
        return {
            getImages: function(params) {
                var parameters = angular.extend({
                    'query': null,
                    'offset': null,
                    'file': null
                }, params)
                return $http({method: 'GET', url: 'api/foodimages/search?' +
                    (params.query ? 'query=' + params.query : '') +
                    (params.offset ? '&offset=' + params.offset : '') +
                    (params.file ? '&file=' + params.file : '')})
                    .then(function(response) {
                        if (typeof response.data === 'object') {
                            return response.data;
                        } else {
                            // invalid response
                            return $q.reject(response.data);
                        }

                    }, function(response) {
                        // something went wrong
                        return $q.reject(response.data);
                    });
            }
        };
    });
