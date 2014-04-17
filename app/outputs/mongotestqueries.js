db.images.aggregate([{$geoNear:
                      {near: [-80, 30],
                       distanceField:
                           "business_info.location.details.coordinate"}}])


