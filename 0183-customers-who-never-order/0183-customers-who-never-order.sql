# Write your MySQL query statement below

#CARA 1
SELECT name as Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.id IS NULL

