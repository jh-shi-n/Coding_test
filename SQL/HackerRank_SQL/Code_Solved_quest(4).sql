# Revising Aggregations - The Count Function
SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000

# Revising Aggregations - The Sum Function
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT LIKE 'California'

# Revising Aggregations - Averages
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT LIKE 'California'

# Japan Population
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE LIKE 'JPN'
