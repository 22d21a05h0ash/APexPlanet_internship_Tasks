-- Total Sales by Item Type
SELECT Item_Type, SUM(Item_Outlet_Sales) AS Total_Sales
FROM bigmart
GROUP BY Item_Type
ORDER BY Total_Sales DESC;

-- Average Sales by Outlet Size
SELECT Outlet_Size, AVG(Item_Outlet_Sales) AS Avg_Sales
FROM bigmart
GROUP BY Outlet_Size;

-- Sales by Location Type
SELECT Outlet_Location_Type, SUM(Item_Outlet_Sales) AS Sales
FROM bigmart
GROUP BY Outlet_Location_Type;

-- Top Performing Outlet Type
SELECT Outlet_Type, SUM(Item_Outlet_Sales) AS Sales
FROM bigmart
GROUP BY Outlet_Type
ORDER BY Sales DESC;