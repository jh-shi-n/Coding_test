#Population Density Difference
SELECT MAX(POPULATION)-MIN(POPULATION)
FROM CITY

#Average Population
SELECT FLOOR(AVG(POPULATION))
FROM CITY

#Employees Salaries
SELECT name
FROM employee
WHERE employee.salary > 2000 AND employee.months < 10
ORDER BY employee.employee_id ASC
