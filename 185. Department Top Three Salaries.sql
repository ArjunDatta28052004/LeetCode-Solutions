# Write your MySQL query statement below
select D.name as Department, E.name as Employee, E.salary as Salary
from Employee E, Department D
where E.departmentId = D.id and 3 > (
    select count(distinct(E2.salary))
    from Employee E2
    where E.departmentId = E2.departmentId and E2.salary>E.salary
)
    
