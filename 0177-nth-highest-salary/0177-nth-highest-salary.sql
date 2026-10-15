CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    
      with highest_salary as(
        select e.salary,
               dense_rank() over(order by e.salary desc) as rn
        from Employee e
      )
      
      select max(hs.salary)
      from highest_salary as hs
      where rn = N
  );
END;
$$ LANGUAGE plpgsql;