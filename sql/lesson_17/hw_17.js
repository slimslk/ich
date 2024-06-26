// 1. Найти все кинотеатры в Калифорнии и посчитать их количество (168)
b.theaters.aggregate([
    {
        $match: {
            "location.geo": {
                $geoWithin: {
                    $geometry: {
                        type: "Polygon",
                        coordinates: [
                            [
                                [
                                    -118.05567936812676,
                                    31.811057461117976
                                ],
                                [
                                    -115.37510650726686,
                                    32.27470819991925
                                ],
                                [
                                    -115.36142146949564,
                                    34.66066432806367
                                ],
                                [
                                    -120.3040420568391,
                                    38.49060420126824
                                ],
                                [
                                    -120.45887281529039,
                                    40.33143764466942
                                ],
                                [
                                    -124.02012504651223,
                                    40.35628824214694
                                ],
                                [
                                    -123.65718733436792,
                                    34.73178183941804
                                ],
                                [
                                    -118.05567936812676,
                                    31.811057461117976
                                ]
                            ]
                        ]
                    }
                }
            }
        }
    },
    {
        $count:
            "Theaters"
    }
])
// Ответ: 168

// 2. Найти недвижимость с самым большим количеством спален (bedrooms) и напишите ее название
db.listingsAndReviews.find({}, {name: 1}).sort({bedrooms: -1}).limit(1)
// Ответ: "Venue Hotel Old City"

// 3. Найти недвижимость с самым высоким рейтингом  review_scores_rating
// при минимальном количестве отзывов 50 (number_of_reviews) и напишите ее название
db.listingsAndReviews.find({
        number_of_reviews: {$gte: 50}
    },
    {
        name: 1,
        _id: 0
}).sort({
    "review_scores.review_scores_rating": -1,
    number_of_reviews: -1
}).limit(1)
// Ответ: "1分鐘到高鐵西九龍站､地鐵柯士甸站､機場和港珠澳大橋巴士A22站    10分鐘到中港城碼頭､海港城"


