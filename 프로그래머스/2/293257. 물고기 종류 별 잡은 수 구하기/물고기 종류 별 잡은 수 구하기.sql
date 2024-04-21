SELECT COUNT(*) AS FISH_COUNT, fi.FISH_NAME
FROM FISH_NAME_INFO fi
JOIN FISH_INFO f 
ON fi.FISH_TYPE = f.FISH_TYPE
GROUP BY fi.FISH_TYPE, fi.FISH_NAME
ORDER BY FISH_COUNT DESC
