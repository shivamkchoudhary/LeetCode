# Write your MySQL query statement below
with cte as
(select sales_id from orders o
left join company c
on o.com_id = c.com_id
where c.name like 'RED')

select name from salesperson
where sales_id not in(
select sales_id from cte)