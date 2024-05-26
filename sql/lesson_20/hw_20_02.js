// 6. Найти рестораны на 'Staten Island' в названии которых есть слово pizza (Pizza и PIZZA тоже считаются)
db.restaurants.aggregate([
    {
        $match: {
            "address.coord": {
                $geoWithin: {
                    $geometry: {
                        type: "Polygon",
                        coordinates: [
                            [
                                [
                                    -74.0788928512484,
                                    40.64785907415061
                                ],
                                [
                                    -74.04705360531808,
                                    40.60431126125424
                                ],
                                [
                                    -74.13569189608097,
                                    40.52985093672891
                                ],
                                [
                                    -74.25465599633755,
                                    40.493401162822096
                                ],
                                [
                                    -74.26225771196188,
                                    40.507514588322735
                                ],
                                [
                                    -74.24959743395449,
                                    40.54128709763435
                                ],
                                [
                                    -74.2146140523255,
                                    40.556485256480634
                                ],
                                [
                                    -74.2011859919876,
                                    40.60488577615938
                                ],
                                [
                                    -74.20311382971705,
                                    40.63082750421219
                                ],
                                [
                                    -74.18423267081381,
                                    40.64692748456705
                                ],
                                [
                                    -74.14672549813987,
                                    40.63846485226815
                                ],
                                [
                                    -74.0788928512484,
                                    40.64785907415061
                                ]
                            ]
                        ]
                    }
                }
            },
            name: /\bpizza\b/i
        }
    }
])

// 7. Выведите названия 5 лучших по среднему значению отзывов ( $avg: "$grades.score")
db.restaurants.aggregate([
    {
        $unwind: {
            path: "$grades"
        }
    },
    {
        $group: {
            _id: "$name",
            avg_score: {
                $avg: "$grades.score"
            }
        }
    },
    {
        $project:
            {
                name: "$_id",
                avg_score: 1,
                _id: 0
            }
    },
    {
        $sort: {
            avg_score: -1
        }
    },
    {
        $limit: 5
    }
])