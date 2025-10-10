# Write your MySQL query statement below
SELECT
    Weather.id
FROM
    Weather
CROSS JOIN
    Weather AS Weather2
WHERE (DATEDIFF(Weather.recordDate, Weather2.recordDate) = 1) AND (Weather.temperature > Weather2.temperature)