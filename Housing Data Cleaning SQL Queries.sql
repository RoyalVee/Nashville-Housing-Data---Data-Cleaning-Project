SELECT TOP (10) *
FROM [Nashville Housing]..Sheet1$;

SELECT TOP (10) *
FROM [Nashville Housing]..Sheet1$_xlnm#_FilterDatabase;




SELECT YearBuilt, COUNT(*) number, MAX(SalePrice)
FROM [Nashville Housing]..Sheet1$
GROUP BY YearBuilt
ORDER BY 2 DESC;


-- Populate Property Address Data





--Breaking out Address into individual Column (Address, City, State)




--Change Y and N to Yes and No in "Sold As Vacant" Field





-- Remove Duplicates 




-- Delete Un-used Column 

