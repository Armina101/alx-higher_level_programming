-- This script lists all records of the second_table having a name value ordered by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
