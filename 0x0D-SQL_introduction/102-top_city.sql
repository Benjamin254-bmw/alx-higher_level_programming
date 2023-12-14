-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp WHERE month=July | month=August ORDER BY avg_temp DESC;
