-- Write your PostgreSQL query statement below
with highest_rank as (
    select score,
           dense_rank() over(order by score desc) as rank_no
    from Scores
)

select score,
       rank_no as rank
from highest_rank