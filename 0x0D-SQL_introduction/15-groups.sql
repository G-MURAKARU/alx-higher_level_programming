-- group entries with same score from second_table
SELECT score, COUNT(score) FROM second_table GROUP BY score ORDER BY score DESC;
