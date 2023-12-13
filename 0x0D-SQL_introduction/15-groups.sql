-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, COUNT(*) FROM second_table AS number GROUP BY score ORDER BY number DESC;
