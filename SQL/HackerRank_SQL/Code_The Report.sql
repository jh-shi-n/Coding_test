#link : https://www.hackerrank.com/challenges/the-report/submissions/code/238498876

SELECT IF(GRADE<8, NULL, NAME) , GRADE, MARKS
FROM Students JOIN Grades
WHERE MARKS BETWEEN Min_Mark and Max_Mark
ORDER BY GRADE DESC, NAME
