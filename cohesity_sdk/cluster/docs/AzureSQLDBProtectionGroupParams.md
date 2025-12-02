# AzureSQLDBProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure SQL DB workload. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdc_data_processing_location** | **str** | Specifies the location where CDC (Change Data Capture) data processing occurs. Valid values are &#39;Server&#39; (processing on SQL DB server) or &#39;Client&#39; (processing on Cohesity cluster). | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_sqldb_tag_ids** | **List[List[int]]** | Array of arrays of SQL DB Tag Ids that specify db instances to Exclude. | [optional] 
**objects** | [**List[AzureSQLDBProtectionGroupObjectParams]**](AzureSQLDBProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**sql_db_tag_ids** | **List[List[int]]** | Array of arrays of SQL DB Tag Ids that specify db instances to Protect. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_sqldb_protection_group_params import AzureSQLDBProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSQLDBProtectionGroupParams from a JSON string
azure_sqldb_protection_group_params_instance = AzureSQLDBProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureSQLDBProtectionGroupParams.to_json())

# convert the object into a dict
azure_sqldb_protection_group_params_dict = azure_sqldb_protection_group_params_instance.to_dict()
# create an instance of AzureSQLDBProtectionGroupParams from a dict
azure_sqldb_protection_group_params_from_dict = AzureSQLDBProtectionGroupParams.from_dict(azure_sqldb_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


