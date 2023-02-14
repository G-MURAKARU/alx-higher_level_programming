-- script: select all entries with a name value, order by descending score from second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
