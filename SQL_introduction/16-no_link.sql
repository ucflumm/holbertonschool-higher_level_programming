-- File 16
-- List all records of the table second_table of the database hbtn_0c_0 in your
-- MySQL server.
-- Requirements:
-- Don't list rows without a name (i.e. NULL name)
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- If scores are equal, order the records by the name (in ascending order)

SELECT `score`, `name` FROM `second_table`
WHERE `name` IS NOT NULL ORDER BY `score` DESC, `name` DESC;