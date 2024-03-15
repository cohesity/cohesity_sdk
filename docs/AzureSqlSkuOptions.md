# AzureSqlSkuOptions

Specifies the SQL SKU parameters which are specific to Azure related Object Protection & Recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int, none_type** | Specifies the capacity of the sku. For azure sql dbs, this is the number of cores. Default value is 4. | [optional] 
**name** | **str, none_type** | Specifies the sku name for azure sql databases and by default Hyperscale is selected. | [optional] 
**tier_type** | **str, none_type** | Specifies the sku tier selection for azure sql databases and by default HS_Gen5 is selected. The tiers must match their sku name selected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


