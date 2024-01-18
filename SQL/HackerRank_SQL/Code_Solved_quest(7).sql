# African Cities
SELECT CITY.NAME
FROM CITY LEFT JOIN COUNTRY
ON(CITY.COUNTRYCODE = COUNTRY.CODE)
WHERE COUNTRY.CONTINENT LIKE 'Africa'

# Average Population of Each Continent
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;