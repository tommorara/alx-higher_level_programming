-- Script to list all shows not categorized under the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    JOIN genres ON tv_show_genres.genre_id = genres.id
    WHERE genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;

