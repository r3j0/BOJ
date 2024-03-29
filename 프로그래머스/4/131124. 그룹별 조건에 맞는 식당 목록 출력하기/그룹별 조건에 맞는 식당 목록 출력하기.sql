-- 코드를 입력하세요
SELECT a.MEMBER_NAME, d.REVIEW_TEXT, DATE_FORMAT(d.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE a
JOIN (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(REVIEW_ID) DESC
    LIMIT 1
) b ON a.MEMBER_ID = b.MEMBER_ID
JOIN REST_REVIEW d ON a.MEMBER_ID = d.MEMBER_ID
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC;