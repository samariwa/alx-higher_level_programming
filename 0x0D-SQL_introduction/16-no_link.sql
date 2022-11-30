-- Does not display nulls
SELECT score, name from second_table WHERE name IS NOT NULL ORDER BY score DESC;

