CREATE DATABASE DATADIGGER;
USE DATADIGGER;

CREATE TABLE CUSTOMER(
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Address VARCHAR(200)
);

-- insert atleast 5 sample customers into the customer tabble.
INSERT INTO CUSTOMER (CustomerID, Name, Email, Address) VALUES
(1, 'Aarav Patel', 'aarav.patel@example.com', 'Ahmedabad, Gujarat'),
(2, 'Kiara Shah', 'kiara.shah@example.com', 'Surat, Gujarat'),
(3, 'Vivaan Mehta', 'vivaan.mehta@example.com', 'Rajkot, Gujarat'),
(4, 'Myra Desai', 'myra.desai@example.com', 'Vadodara, Gujarat'),
(5, 'Reyansh Joshi', 'reyansh.joshi@example.com', 'Bhavnagar, Gujarat');

-- retrive all customers details 
SELECT * FROM CUSTOMER;

-- update a customer address
UPDATE CUSTOMER
SET Address = 'Gandhinagar, Gujarat'
WHERE CustomerID = 1;

-- delete a customer using their CustomerID
DELETE FROM CUSTOMER
WHERE CustomerID = 1;

-- display all customers whose name is 'Alice'
SELECT * FROM CUSTOMER
WHERE Name = 'Alice';


CREATE TABLE ORDERS(
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(8,2),
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID)
);

-- insert atleast 5 sample orders into the orders tabble.
INSERT INTO ORDERS (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 1, '2024-01-15', 150.00),
(2, 2, '2024-02-20', 200.00),
(3, 3, '2024-03-10', 300.00),
(4, 4, '2024-04-05', 250.00),
(5, 1, '2024-05-12', 100.00);

-- retrive all orders made by a specific customer  
SELECT * FROM ORDERS
WHERE CustomerID = 3;

-- update an order's total amount
UPDATE ORDERS
SET TotalAmount = 350.00
WHERE OrderID = 3;

-- delete an order using its OrderID
DELETE FROM ORDERS
WHERE OrderID = 5;

-- retrieve orders placed in last 30 days
SELECT * FROM ORDERS
WHERE OrderDate >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

-- retrieve the highest, lowest and average order amount using aggregate functions
SELECT 
    MAX(TotalAmount) AS HighestOrderAmount,
    MIN(TotalAmount) AS LowestOrderAmount,
    AVG(TotalAmount) AS AverageOrderAmount
FROM ORDERS;


CREATE TABLE PRODUCT(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(8,2),
    Stock INT
);

-- insert atleast 5 sample products into the product tabble.
INSERT INTO PRODUCT (ProductID, ProductName, Price, Stock) VALUES
(1, 'Laptop', 800.00, 50),
(2, 'Smartphone', 500.00, 100),
(3, 'Headphones', 150.00, 200),
(4, 'Smartwatch', 200.00, 150),
(5, 'Tablet', 300.00, 80);

-- retrive all products sorted by price in descending order
SELECT * FROM PRODUCT
ORDER BY Price DESC;

-- update the price of specific product 
UPDATE PRODUCT
SET Price = 750.00
WHERE ProductName = 'Laptop';

-- delete product of it's out of stock 
DELETE FROM PRODUCT 
WHERE Stock = 0;

-- retrive products with price between rs. 500 and rs. 2000
SELECT ProductName, Price FROM PRODUCT
WHERE Price BETWEEN 500 AND 2000;

-- retrive the most expensive and cheapest product using MAX() and MIN().
SELECT 
    MAX(Price) AS MostExpensiveProduct,
    MIN(Price) AS CheapestProduct
FROM PRODUCT;


CREATE TABLE ORDERDETAILS(
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SubTotal DECIMAL(8,2),
    FOREIGN KEY (OrderID) REFERENCES ORDERS(OrderID),
    FOREIGN KEY (ProductID) REFERENCES PRODUCT(ProductID)
);

-- insert atleast 5 sample order details into the orderdetails table
INSERT INTO ORDERDETAILS (OrderDetailID, OrderID, ProductID, Quantity, SubTotal) VALUES
(1, 1, 1, 1, 800.00),
(2, 1, 3, 2, 300.00),
(3, 2, 2, 1, 500.00),
(4, 3, 4, 1, 200.00),
(5, 4, 5, 2, 600.00);

-- retrive order details for a specific order
SELECT * FROM ORDERDETAILS
WHERE OrderID = 1;

-- calculate the total revenue generated from all oredrs using SUM()
SELECT SUM(SubTotal) AS TotalRevenue
FROM ORDERDETAILS;

-- retrieve the top 3 most ordered products
SELECT ProductID, SUM(Quantity) AS TotalQuantity
FROM ORDERDETAILS
GROUP BY ProductID
ORDER BY TotalQuantity DESC
LIMIT 3;

-- count how many times a specific product has been sold using COUNT()
SELECT COUNT(*) AS TimesSold
FROM ORDERDETAILS
WHERE ProductID = 1;