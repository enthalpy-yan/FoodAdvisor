db.images.aggregate([{$geoNear:
                      {near: [-80, 30],
                       distanceField:
                           "business_info.location.details.coordinate"}}])

db.images.aggregate([{$project: {category: '$business_info.category'}},
                     {$unwind: '$category'},
                     {$match: {category: {$regex: /^a/, $options: 'i'}}},
                     {$sort: {rating: -1}},
                     {$limit: 15}])

