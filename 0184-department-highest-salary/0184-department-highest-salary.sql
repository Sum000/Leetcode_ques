-- Write your PostgreSQL query statement below
with highest_salary as (
    select e.id,
           e.name as Employee,
           e.salary as Salary,
           e.departmentId,
           d.name as Department,
           rank() over(partition by d.name order by e.salary desc) as rn
    from Employee e
    join Department d 
    on e.departmentId = d.id
)


select Department,
       Employee,
       Salary 
from highest_salary
where rn = 1
     
       