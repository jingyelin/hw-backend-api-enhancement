# hw-backend-api-enhancement

## API spec
1. Get lineItem/UnblendedCost grouping by product/productname
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
   
2. Get daily lineItem/UsageAmount grouping by product/productname
, API URLs, and DB schema
