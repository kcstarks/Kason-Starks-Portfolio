
--What are the columns and values?
SELECT TOP 10 *
FROM dbo.grocery_sales


--Just one state?
SELECT DISTINCT State 
FROM dbo.grocery_sales



--We can group by different columns to see profit trends
SELECT DISTINCT Category, COUNT(Order_ID) AS order_count, SUM(Sales) AS sales_sum, SUM(Profit) AS profit_sum, ((SUM(Profit)/SUM(Sales))*100) AS profit_sale_percent, (SUM(Profit)/COUNT(Order_ID)) AS profit_by_order_count
INTO sales_by_category
FROM dbo.grocery_sales
GROUP BY Category
ORDER BY profit_sum

SELECT DISTINCT Sub_Category, COUNT(Order_ID) AS order_count, SUM(Sales) AS sales_sum, SUM(Profit) AS profit_sum, ((SUM(Profit)/SUM(Sales))*100) AS profit_sale_percent, (SUM(Profit)/COUNT(Order_ID)) AS profit_by_order_count
INTO sales_by_subcategory
FROM dbo.grocery_sales
GROUP BY Sub_Category
ORDER BY profit_sum

SELECT DISTINCT City, COUNT(Order_ID) AS order_count, SUM(Sales) AS sales_sum, SUM(Profit) AS profit_sum, ((SUM(Profit)/SUM(Sales))*100) AS profit_sale_percent, (SUM(Profit)/COUNT(Order_ID)) AS profit_by_order_count
INTO sales_by_city
FROM dbo.grocery_sales
GROUP BY City
ORDER BY profit_sum

SELECT DISTINCT Region, COUNT(Order_ID) AS order_count, SUM(Sales) AS sales_sum, SUM(Profit) AS profit_sum, ((SUM(Profit)/SUM(Sales))*100) AS profit_sale_percent, (SUM(Profit)/COUNT(Order_ID)) AS profit_by_order_count
INTO sales_by_region
FROM dbo.grocery_sales
GROUP BY Region
ORDER BY profit_sum

--If the customer data involved other companies like manufacturers, distributors, suppliers, etc. as opposed to individual consumers, then this query would be more appropriate
SELECT DISTINCT Customer_Name, COUNT(Order_ID) AS order_count, SUM(Sales) AS sales_sum, SUM(Profit) AS profit_sum, ((SUM(Profit)/SUM(Sales))*100) AS profit_sale_percent, (SUM(Profit)/COUNT(Order_ID)) AS profit_by_order_count
INTO sales_by_customer
FROM dbo.grocery_sales
GROUP BY Customer_Name
ORDER BY profit_sum



--We need to change the date column from year/month/day to year
SELECT Order_ID,
	Customer_Name,
	Category,
	Sub_Category,
	City,
	YEAR(Order_Date) AS date_year,
	Region,
	Sales,
	Discount,
	Profit
INTO grocery_sales_year
FROM dbo.grocery_sales



--Growth Percentage every Year
SELECT date_year, SUM(Sales) AS sales_sum, SUM(Profit) AS profit_sum, (SUM(Profit) - LAG(SUM(Profit)) OVER (ORDER BY date_year ASC)) AS profit_growth, (SUM(Profit) - LAG (SUM(Profit)) OVER (ORDER BY date_year ASC))/LAG (SUM(Profit)) OVER (ORDER BY date_year ASC)*100 AS profit_percentage_growth
INTO growth
FROM dbo.grocery_sales_year
GROUP BY date_year
ORDER BY profit_sum DESC;
