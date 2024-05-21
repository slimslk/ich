// 1. Найдите трек с наивысшими показателями  Danceability и Energy.
db.Spotify_Youtube.find({}, {}).sort({"Danceability": -1, "Energy": -1})

// 2. У какого трека (но не compilation) самая большая длительность?
db.Spotify_Youtube.find({Album_type: {$ne: "compilation"}}).sort({Duration_ms: -1}).limit(1)
// Ответ: 'Ocean Waves for Sleep'

// 3. В каком одном альбоме самое большее количество треков?
db.Spotify_Youtube.aggregate([
    {
        $group:
            {
                _id: "$Album",
                amount_of_tracks: {
                    $sum: 1
                }
            }
    },
    {
        $sort:
            {
                amount_of_tracks: -1
            }
    },
    {
        $limit: 1
    }
])
// Ответ: "Greatest Hits"

// 4. Сколько просмотров видео на youtube у трека с самым высоким количеством прослушиваний на spotify (Stream)?
db.Spotify_Youtube.aggregate([
    {
        $sort: {
            Stream: -1
        }
    },
    {
        $limit: 1
    },
    {
        $project: {
            Views: 1,
            _id: 0
        }
    }
])
// Ответ: 674164500

// 5. Экспортируйте 20 самых популярных (прослушивания или просмотры) треков по версиям youtube и spotify
// и импортируйте в базу ich_edit их с именами top20youtube и top20spotify, и добавьте им свои имена для уникальности.
db.getCollection('Spotify_Youtube').aggregate(
    [{$sort: {Views: -1}}, {$limit: 20}],
    {maxTimeMS: 60000, allowDiskUse: true}
);

db.getCollection('Spotify_Youtube').aggregate(
    [{$sort: {Stream: -1}}, {$limit: 20}],
    {maxTimeMS: 60000, allowDiskUse: true}
);