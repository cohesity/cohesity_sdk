# AzureSqlSkuOptions

Specifies the SQL SKU parameters which are specific to Azure related Object Protection & Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | Specifies the capacity of the sku. For azure sql dbs, this is the number of cores. Default value is 4. | [optional] 
**name** | **str** | Specifies the sku name for azure sql databases and by default Hyperscale is selected. | [optional] 
**tier_type** | **str** | Specifies the sku tier selection for azure sql databases and by default HS_Gen5 is selected. The tiers must match their sku name selected. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_sku_options import AzureSqlSkuOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlSkuOptions from a JSON string
azure_sql_sku_options_instance = AzureSqlSkuOptions.from_json(json)
# print the JSON string representation of the object
print(AzureSqlSkuOptions.to_json())

# convert the object into a dict
azure_sql_sku_options_dict = azure_sql_sku_options_instance.to_dict()
# create an instance of AzureSqlSkuOptions from a dict
azure_sql_sku_options_from_dict = AzureSqlSkuOptions.from_dict(azure_sql_sku_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


