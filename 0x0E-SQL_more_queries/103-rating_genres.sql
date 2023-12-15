-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT tv_genres.name,
       SUM(tv_show_ratings.rate) AS rating
       FROM tv_show_genres
       LEFT JOIN tv_show_ratings
       ON tv_show_genres.show_id=tv_show_ratings.show_id
       LEFT JOIN tv_genres
       ON tv_show_genres.genre_id=tv_genres.id
       GROUP BY tv_genres.name
       ORDER BY rating
       DESC;
