-- 코드를 입력하세요
SELECT b.CATEGORY, sum(s.SALES) TOTAL_SALES
FROM BOOK b
JOIN BOOK_SALES s
ON b.BOOK_ID = s.BOOK_ID
WHERE date_format(s.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY b.CATEGORY
ORDER BY b.CATEGORY;