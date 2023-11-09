-- 코드를 입력하세요
SELECT  ORDER_ID, 
        PRODUCT_ID, 
        date_format(OUT_DATE, '%Y-%m-%d') OUT_DATE, 
        if(OUT_DATE is null, '출고미정', if('2022-05-01' < OUT_DATE, '출고대기', '출고완료')) 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;