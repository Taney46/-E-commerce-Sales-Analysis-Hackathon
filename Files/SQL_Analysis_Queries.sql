CREATE DATABASE hackathon;
USE hackathon;

SELECT * FROM ecommerce;

-- What are the total sales by region?

SELECT Region, SUM(TotalPrice) AS TotalRevenue
FROM ecommerce
GROUP BY Region
ORDER BY TotalRevenue DESC;

-- Which product category generates the highest revenue? 

SELECT Category, SUM(TotalPrice) AS TotalRevenue
FROM ecommerce
GROUP BY Category
ORDER BY TotalRevenue DESC
LIMIT 810;

-- What is the average shipping fee by region?

SELECT Region, ROUND(AVG(ShippingFee), 2) AS AvgShippingFee
FROM ecommerce
GROUP BY Region
ORDER BY AvgShippingFee DESC;

-- How does customer age impact purchasing behavior?

SELECT Age, COUNT(CustomerID) AS TotalOrders, ROUND(AVG(TotalPrice), 2) AS AvgSpent
FROM ecommerce
GROUP BY Age
ORDER BY Age;

-- What is the most popular product by gender?

SELECT Gender, ProductName, COUNT(ProductName) AS PurchaseCount
FROM ecommerce
GROUP BY Gender, ProductName
ORDER BY PurchaseCount DESC
LIMIT 10000;

-- What is the order fulfillment rate (delivered vs. returned)? 

SELECT ShippingStatus, COUNT(*) AS OrderCount, 
       ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce)), 2) AS Percentage
FROM ecommerce
GROUP BY ShippingStatus;


