-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name FROM second_table ORDER BY score DESC WHERE score >= 10;
