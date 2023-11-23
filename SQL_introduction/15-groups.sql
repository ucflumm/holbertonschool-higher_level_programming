-- File 15
-- List the number of records with the same score in the table second_table.
-- The result should display the score and the number of records for this score
-- with the label number
-- List should be sorted by number of records in descending order

SELECT `score`, COUNT(`score`) AS `number` FROM `second_table`
GROUP BY `score` ORDER BY `number` DESC;