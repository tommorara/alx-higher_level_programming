-- Script to list all cities of California in the hbtn_0d_usa database
-- Uses a subquery to match the state_id with California's id in the states table
-- Results are sorted in ascending order by cities.id
-- JOIN keyword is not used as per the requirement

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

