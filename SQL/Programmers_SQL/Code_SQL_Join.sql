# 없어진 기록 찾기
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS AS OUTS LEFT OUTER JOIN ANIMAL_INS AS INS
ON (OUTS.ANIMAL_ID = INS.ANIMAL_ID)
WHERE INS.ANIMAL_ID IS NULL

#Outer Join(왼쪽)
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS
ON (INS.ANIMAL_ID = OUTS.ANIMAL_ID)
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME ASC

#  Outer Join, Is Null, Limit
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS
ON (INS.ANIMAL_ID = OUTS.ANIMAL_ID)
WHERE OUTS.DATETIME IS NULL
ORDER BY INS.DATETIME
LIMIT 3;

# IFNULL, 문자열 관련
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, IFNULL(I.NAME,"No name")
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O
ON(I.ANIMAL_ID = O.ANIMAL_ID)
WHERE I.SEX_UPON_INTAKE LIKE '%Intact%' and O.SEX_UPON_OUTCOME NOT LIKE '%Intact%'
order by I.ANIMAL_ID
