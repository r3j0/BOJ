-- 코드를 입력하세요
SELECT (floor(PRICE/10000)*10000) PRICE_GROUP, count(*) PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;