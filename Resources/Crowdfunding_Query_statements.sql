Select * FROM "campaign";

Select * FROM "category";

Select * FROM "contacts";

Select * FROM "subcategory";

--Merge multiple tables to create a new table--
Select cp.contact_id, cp.company_name, cp.description, cat.category, sc.subcategory, ct.email
FROM "campaign" as cp
INNER JOIN "contacts" as ct ON
cp.contact_id=ct.contact_id
INNER JOIN "category" as cat ON
cat.category_id=cp.category_id
INNER JOIN "subcategory" as sc ON
sc.subcategory_id=cp.subcategory_id;
