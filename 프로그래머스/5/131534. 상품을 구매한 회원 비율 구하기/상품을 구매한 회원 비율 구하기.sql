SELECT year(sales_date) as year, month(sales_date) as month,
    count(distinct user_id) as purchased_users,
    round(count(distinct user_id)/(select count(*)
                                   from user_info
                                   where year(joined) = 2021),1)
    AS purchased_ratio
FROM online_sale
WHERE user_id in (select user_id from user_info where year(joined) = 2021)
GROUP BY year(sales_date), month(sales_date)
ORDER BY year, month
