-- Script to list all cities along with their states in the hbtn_0d_usa database
-- Displays each record as cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

