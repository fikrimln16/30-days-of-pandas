# Write your MySQL query statement below

SELECT s.name
FROM salesperson s
LEFT JOIN orders o ON (o.sales_id=s.sales_id)
LEFT JOIN company c ON (o.com_id=c.com_id)
GROUP BY s.name
HAVING COUNT(order_id)=0 OR NOT SUM(c.name='RED')>0