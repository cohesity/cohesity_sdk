# AzureCosmosDBNoSQLProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure CosmosDB NoSQL workload. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cosmos_dbno_sql_tag_ids** | **[[int]], none_type** | Array of arrays of CosmosDB NoSQL Tag Ids that specify db instances to Protect. | [optional] 
**exclude_cosmos_dbno_sql_tag_ids** | **[[int]], none_type** | Array of arrays of CosmosDB NoSQL Tag Ids that specify db instances to Exclude. | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[AzureCosmosDBNoSQLProtectionGroupObjectParams]**](AzureCosmosDBNoSQLProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


