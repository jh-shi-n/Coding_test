# 특정 단어 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('LUCY','ELLA','PICKLE','ROGAN','SABRINA','MITTY')
ORDER BY ANIMAL_ID

# 문자열 내 특정 단어 포함 여부 확인
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' and NAME LIKE '%EL%'
ORDER BY NAME

# 특정 조건 만족하는지 확인 (1)
SELECT ANIMAL_ID,  NAME, IF(SEX_UPON_INTAKE LIKE 'Intact%', "X", "O")
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

# 특정 조건 만족하는지 확인 (2)
SELECT O.ANIMAL_ID, LOWER(O.NAME)
FROM ANIMAL_INS AS I RIGHT JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY O.DATETIME - I.DATETIME DESC
LIMIT 2;

# 형 변환(날짜)
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d")AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
