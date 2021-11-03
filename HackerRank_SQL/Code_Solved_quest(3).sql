#Weather Observation Station 8
SELECT CITY
FROM STATION
WHERE LEFT(CITY, 1) IN ('a','e','i','o','u')
and RIGHT(CITY,1) IN ('a','e','i','o','u')

#Weather Observation Station 9
SELECT DISTINCT(CITY)
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u')

#Weather Observation Staion 10
SELECT DISTINCT(CITY)
FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','e','i','o','u')

#Weather Observation Staion 11
SELECT DISTINCT(CITY)
FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','e','i','o','u')
OR LEFT(CITY,1) NOT IN ('a','e','i','o','u')

#Weather Observation Station 12
SELECT DISTINCT(CITY)
FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','e','i','o','u') and LEFT(CITY,1) NOT IN ('a','e','i','o','u') 

#Higher Than 75 Marks
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75 
ORDER BY RIGHT(NAME,3), ID ASC
