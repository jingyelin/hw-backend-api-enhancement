# hw-backend-api-enhancement

## API spec
1. Get lineItem/UnblendedCost grouping by product/productname
   - Method:  GET
   - path:  /app/unblended_cost
   - Input
     | Column | Required | Type | Note |
     | ------ | -------- | -------- | -------- |
     | usageaccountid | true | String | lineitem/usageaccountid	|
     | page | false | int | page number  |
	page要為數字，可以不填,每一頁最多顯示5筆資料, 如果傳入非數字，系統會回傳第一頁, 如果沒傳入值，系統會回傳第一頁
    - Output 
     
     ```JSON
       {
        "{product/productname_A}": "sum(lineitem/unblendedcost)",
        "{product/productname_B}": "sum(lineitem/unblendedcost)",
        ...
        }
      ```

   - API URL
      http://127.0.0.1:8000/app/unblended_cost/?usageaccountid=AccountID&page=PageNumber
      
      Example:
      http://127.0.0.1:8000/app/unblended_cost/?usageaccountid=484234319610&page=2

2. Get daily lineItem/UsageAmount grouping by product/productname
   - Method: GET
   - path:  /app/usage_amount
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
## Performance
1. 在統計prodname的 unblendedCost
在db查詢時直接 group by  prodname 再用sum函數來統計unblendedCost

2. 在統計prodname的每日usageAmount
	1. 將查詢結果依 prodname和usagestartdate排序
	2. for loop 查詢結果來建立兩層的 dictionary
	
		第一層的dictionary 
		- key 是 prodname
		- value 是 第二層的dictionary
	
		第二層dictionary 記錄 此prodname 每日的usageAmount總量
		- key 是日期
		- value 是 每日的usageAmount總量
