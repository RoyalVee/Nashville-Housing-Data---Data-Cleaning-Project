SELECT TOP (10) *
FROM [Nashville Housing]..Sheet1$;

SELECT TOP (10) *
FROM [Nashville Housing]..Sheet1$_xlnm#_FilterDatabase;




SELECT YearBuilt, COUNT(*) number, MAX(SalePrice)
FROM [Nashville Housing]..Sheet1$
GROUP BY YearBuilt
ORDER BY 2 DESC;



-- Formate the SaleDate Column to Date type

SELECT nh.SaleDate, CONVERT(Date, nh.SaleDate)
FROM [Nashville Housing]..Sheet1$ nh


Update [Nashville Housing]..Sheet1$
SET SaleDate = CONVERT(Date, SaleDate)

SELECT nh.SaleDate
FROM [Nashville Housing]..Sheet1$ nh

ALter Table [Nashville Housing]..Sheet1$
Add SaleDateFormated Date;


Update [Nashville Housing]..Sheet1$
SET SaleDateFormated = CONVERT(Date, SaleDate)


SELECT nh.SaleDateFormated
FROM [Nashville Housing]..Sheet1$ nh



-- Populate Property Address Data





--Breaking out Address into individual Column (Address, City, State)




--Change Y and N to Yes and No in "Sold As Vacant" Field





-- Remove Duplicates 




-- Delete Un-used Column 

