WITH ok AS (
    SELECT *,
           CASE WHEN DATEDIFF(customer_pref_delivery_date, order_date) < 1 THEN 1.0 ELSE 0 END AS immediate,
           CASE WHEN DATEDIFF(customer_pref_delivery_date, order_date) >= 1 THEN 1.0 ELSE 0 END AS scheduled
    FROM Delivery
)

SELECT ROUND(AVG(immediate)*100,2) as 'immediate_percentage'
FROM ok

