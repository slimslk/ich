// 1. Из коллекции sample_airbnb.listingsAndReviews найдите среднюю цену за сутки проживания на Гавайских островах.
db.listingsAndReviews.aggregate(
[
    {
        $match: {
            "address.location": {
                $geoWithin: {
                    $centerSphere: [
                        [
                            -157.65702632774844,
                            20.00634867072947
                        ],
                        0.07959095868810681
                    ]
                }
            }
        }
    },
    {
        $group:
            {
                _id: null,
                mean_price: {
                    $avg: "$price"
                }
            }
    }
])
// Ответ: 231.4853420195439739413680781758958


// 2. Подсчитайте в коллекции sample_mflix.movies, сколько фильмов имеют imdb рейтинг выше 8 и выходили в период
// с 2015 до 2023 года (используем year)
db.movies.find({year: {$gte: 2015, $lt: 2023}, "imdb.rating": {$gt: 8}}).count()
// Ответ: 53

// Какой из них имеет самый высокий рейтинг?
db.movies.find({
        year: {$gte: 2015, $lt: 2023},
        "imdb.rating": {$gt: 8}
    },
    {
        title: 1, _id: 0
}).sort({
        "imdb.rating": -1
}).limit(1)
// Ответ: "A Brave Heart: The Lizzie Velasquez Story", рейтинг - 9.4