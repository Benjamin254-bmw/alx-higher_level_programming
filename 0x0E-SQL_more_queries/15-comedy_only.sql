-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_shows.title
       FROM tv_show_genres
       LEFT JOIN tv_shows
       ON tv_show_genres.show_id=tv_shows.id
       LEFT JOIN tv_genres
       ON tv_show_genres.genre_id=tv_genres.id
       WHERE tv_genres.name='Comedy'
       ORDER BY tv_shows.title
       ASC;
