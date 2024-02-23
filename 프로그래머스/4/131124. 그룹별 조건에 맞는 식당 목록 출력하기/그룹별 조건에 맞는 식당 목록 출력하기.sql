SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d")
FROM MEMBER_PROFILE M
JOIN (
    SELECT REVIEW_TEXT, REVIEW_DATE, MEMBER_ID
    FROM REST_REVIEW
    WHERE MEMBER_ID = (
        SELECT MEMBER_ID
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY COUNT(*) DESC
        LIMIT 1)
    ) R
ON R.MEMBER_ID = M.MEMBER_ID
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT