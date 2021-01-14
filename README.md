# hw-backend-api-enhancement

## API spec
1. Get lineItem/UnblendedCost grouping by product/productname
   - Method 
      
      GET
   - path
     
     /app/unblended_cost
   - Input
     | Column | Required |
     | ------ | -------- |
     | usageaccountid | true |
    - Output 
     
     ```JSON
       {
        "{product/productname_A}": "sum(lineitem/unblendedcost)",
        "{product/productname_B}": "sum(lineitem/unblendedcost)",
        ...
        }
      ```

   - API URL
      http://127.0.0.1:8000/app/unblended_cost/?usageaccountid=AccountID
      
      Example:
      http://127.0.0.1:8000/app/unblended_cost/?usageaccountid=484234319610

2. Get daily lineItem/UsageAmount grouping by product/productname
   - Method 
      GET
   - path
     /app/usage_amount
   - Input
     | Column | Required |
     | ------ | -------- |
     | usageaccountid | true |
    - Output
    ```JSON
       {
         "{product/productname_A}": {
            "YYYY/MM/01": "sum(lineItem/UsageAmount)",
            "YYYY/MM/02": "sum(lineItem/UsageAmount)",
            "YYYY/MM/03": "sum(lineItem/UsageAmount)",
            ...
          },
          "{product/productname_B}": {
             "YYYY/MM/01": "sum(lineItem/UsageAmount)",
             "YYYY/MM/02": "sum(lineItem/UsageAmount)",
             "YYYY/MM/03": "sum(lineItem/UsageAmount)",
             ...
           },
        }
      ```
      
    - API URL
      http://127.0.0.1:8000/app/usage_amount/?usageaccountid=AccountID
      
      Example:
      http://127.0.0.1:8000/app/usage_amount/?usageaccountid=484234319610

## DB schema
1. Create 1 table, table name: tab
```sql
CREATE TABLE "tab" (
	"field1"	INTEGER NOT NULL,
	"bill/PayerAccountId"	TEXT,
	"lineItem/UsageAccountId"	TEXT,
	"lineItem/UsageStartDate"	TEXT,
	"lineItem/UsageEndDate"	TEXT,
	"lineItem/UsageAmount"	REAL,
	"lineItem/UnblendedRate"	REAL,
	"lineItem/UnblendedCost"	REAL,
	"product/ProductName"	TEXT,
	PRIMARY KEY("field1")
)
```
2. Create 1 DB index to enhance query performance
```sql
CREATE INDEX "tab_usage_account_id_product_name" ON "tab" (
	"lineItem/UsageAccountId",
	"product/ProductName"
)
```
