-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT DISTINCT tv_genres.name
       FROM tv_show_genres
       LEFT JOIN tv_shows
       ON tv_show_genres.show_id=tv_shows.id
       LEFT JOIN tv_genres
       ON tv_show_genres.genre_id=tv_genres.id
       WHERE tv_genres.name NOT IN
         (SELECT tv_genres.name
	   FROM tv_show_genres
	   LEFT JOIN tv_shows
	   ON tv_show_genres.show_id=tv_shows.id
	   LEFT JOIN tv_genres
	   ON tv_show_genres.genre_id=tv_genres.id
	   WHERE tv_shows.title='Dexter')
	ORDER BY tv_genres.name;
