create database DataTransformer;
use DataTransformer;

create table Customers(
	CustomerID int primary key,
    FirstName varchar(100),
    LastName varchar(100),
    Email varchar(50),
    RegistrationDate date
);

create table Orders(
	OrderId int primary key,
    CustomerID int,
    OrderDate date,
    TotalAmount decimal(10,2),
    foreign key (CustomerID) references Customers(CustomerID)
);

create table Employees(
	EmployeeID int primary key,
    FirstName varchar(100),
    LastName varchar(100),
    Department varchar(50),
    HireDate date,
    Salary decimal(10,2)
);

insert into Customers values
(1, 'Ramesh', 'Patel', 'ramesh.patel@example.com', '2023-01-15'),
(2, 'Nirali', 'Shah', 'nirali.shah@example.com', '2023-02-10'),
(3, 'Ketan', 'Joshi', 'ketan.joshi@example.com', '2023-03-05'),
(4, 'Bhavna', 'Mehta', 'bhavna.mehta@example.com', '2023-04-20'),
(5, 'Suresh', 'Trivedi', 'suresh.trivedi@example.com', '2023-05-12'),
(6, 'Pooja', 'Desai', 'pooja.desai@example.com', '2023-06-18'),
(7, 'Manish', 'Modi', 'manish.modi@example.com', '2023-07-25'),
(8, 'Hetal', 'Parmar', 'hetal.parmar@example.com', '2023-08-30'),
(9, 'Jayesh', 'Bhatt', 'jayesh.bhatt@example.com', '2023-09-14'),
(10, 'Ankita', 'Rathod', 'ankita.rathod@example.com', '2023-10-01');

insert into Orders values
(101, 1, '2023-02-01', 2500.00),
(102, 2, '2023-02-15', 1800.50),
(103, 3, '2023-03-10', 3200.75),
(104, 4, '2023-04-25', 1500.00),
(105, 5, '2023-05-20', 2750.25),
(106, 6, '2023-06-22', 4200.00),
(107, 7, '2023-07-28', 1999.99),
(108, 8, '2023-09-01', 3500.00),
(109, 9, '2023-09-20', 2899.50),
(110, 10, '2023-10-05', 4100.00),
(111, 1, '2023-11-10', 3200.00),
(112, 2, '2023-11-15', 1800.00),
(113, 3, '2023-12-01', 3000.50),
(114, 4, '2023-12-10', 2000.00),
(115, 5, '2023-12-15', 3500.75),
(116, 6, '2023-12-20', 4200.00),
(117, 7, '2023-12-22', 1900.50),
(118, 8, '2023-12-25', 3400.00),
(119, 9, '2023-12-28', 3100.25),
(120, 10, '2023-12-30', 4300.50);

insert into Employees values
(201, 'Dharmesh', 'Patel', 'Sales', '2022-01-10', 35000.00),
(202, 'Sneha', 'Shah', 'HR', '2022-02-15', 28000.00),
(203, 'Rajesh', 'Joshi', 'IT', '2022-03-20', 45000.00),
(204, 'Meena', 'Mehta', 'Finance', '2022-04-25', 40000.00),
(205, 'Prakash', 'Trivedi', 'Marketing', '2022-05-30', 37000.00),
(206, 'Kavita', 'Desai', 'Support', '2022-06-18', 25000.00),
(207, 'Nilesh', 'Modi', 'Sales', '2022-07-22', 36000.00),
(208, 'Hiral', 'Parmar', 'IT', '2022-08-28', 47000.00),
(209, 'Jignesh', 'Bhatt', 'Finance', '2022-09-12', 39000.00),
(210, 'Anita', 'Rathod', 'HR', '2022-10-05', 30000.00);

-- INNER JOIN : retrive all orders and customers details where order exists.
select o.OrderId,
       o.OrderDate,
	   o.TotalAmount,
       c.CustomerID,
       c.FirstName,
       c.LastName,
       c.Email,
       c.RegistrationDate
from orders o
inner join customers c
on o.CustomerID = c.CustomerID;

-- LEFT JOIN : retrive all customers and their corresponding orders (if any).
select c.CustomerID,
       c.FirstName,
       c.LastName,
       c.Email,
       c.RegistrationDate,
       o.OrderId,
	   o.TotalAmount
from orders o
left join customers c
on o.CustomerID = c.CustomerID;

-- RIGHT JOIN : retrive all orders and their corresponding customer (if any).
select o.OrderId,
       o.OrderDate,
       o.TotalAmount,
       c.CustomerID,
       c.FirstName,
       c.LastName,
       c.Email,
       c.RegistrationDate
from orders o
right join customers c
on o.CustomerID = c.CustomerID;

-- FULL OUTER JOIN : retrive al customers and all orders, regardless of matching 
select c.FirstName,
       c.LastName,
       o.OrderId,
       o.OrderDate,
       o.TotalAmount
from orders o
left join customers c
on o.CustomerID = c.CustomerID
union
select c.FirstName,
       c.LastName,
       o.OrderId,
       o.OrderDate,
       o.TotalAmount
from orders o
right join customers c
on o.CustomerID = c.CustomerID;

-- subquery to find the customers who have placed orders worh more than the average amount.
select FirstName, LastName, Email from Customers
where CustomerID in (select CustomerID from Orders where TotalAmount > (select avg(TotalAmount) from orders));

-- subquery to find employees with salaries above the average salary.
select FirstName, LastName, Department, Salary from EMployees 
where Salary > (select avg(Salary) from Employees);

-- extract the year and month from the OrderDate.
select OrderID, CustomerID, year(OrderDate) as ODyear, monthname(OrderDate) as ODmonth from Orders;

-- calculate the difference in days between two dates (order date and current date).
select OrderID, OrderDate, datediff(current_date(), OrderDate) as Order_Days from Orders;

-- format the OrderDate to a readable fprmat (e.g., 'DD-MM-YYYY').
select OrderID, OrderDate, date_format(OrderDate, '%d-%b-%y') from Orders;

-- concatenate FristName and LastName to form a full name.
select FirstName, LastName, concat(FirstName, ' ', LastName) as Full_Name from Customers;

-- replace part of a string (e.g., replace 'John' with 'Jonathan').
select FirstName, LastName, replace(FirstName, 'Ramesh', 'Chagan') as Modification from Customers;

-- convert FirstName to Uppercase and LastName to lowercase.
select FirstName, LastName, upper(FirstName), lower(LastName) from Customers;

-- trim extra space from the email field.
select Email, trim(Email) from Customers;

-- calsulate the running total of TotalAmount for each order.
select OrderID, OrderDate, TotalAmount, sum(TotalAmount) over (order by OrderDate) as Running_Total from Orders;

-- rank orders based on TotaAmount using the RANK() function.
select OrderID, OrderDate, TotalAmount, rank() over (order by TotalAmount) as Order_Rank  from Orders;

-- assign a discount based on TotalAmount in irders (e.g., >1000: 10% off, >500: 5% off).
select OrderID, OrderDate, TotalAmount,
	   case 
           when TotalAmount > 500 then TotalAmount*0.05
           when TotalAmount > 1000 then TotalAmount*0.10
           else 0
       end as Discount 
from orders;

-- categorize employees' salaries as high, medium, or low.
select FirstName, LastName, Salary,
       case
           when Salary > 60000 then 'HIgh'
           when Salary > 40000 then 'Medium'
           else 'Low'
	   end as Category_Salary
from Employees;