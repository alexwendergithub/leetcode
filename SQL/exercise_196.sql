# Write your MySQL query statement below
DELETE
    Person
FROM
    Person
JOIN
    Person as Person2
ON Person.email = Person2.email AND Person.id>Person2.id