# Weather Observation Station 4
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION

# Weather Observation Station 5
SELECT city, length(city) FROM station
ORDER BY length(city),city ASC
LIMIT 1;

SELECT city, length(city) FROM station
ORDER BY length(city) DESC
LIMIT 1;

# Weather Observation Station 6
SELECT DISTINCT CITY
FROM STATION
WHERE (city LIKE 'A%'
       OR city LIKE 'E%'
       OR city LIKE 'I%'
       OR city LIKE 'O%'
       OR city LIKE 'U%'
);
