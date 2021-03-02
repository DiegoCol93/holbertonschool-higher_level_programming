-- Lists all cities in the database.
SELECT cities.id, cities.name, states.name
FROM cities, states
where cities.state_id = states.id
