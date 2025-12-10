# AzureMySQLProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure MySQL workload. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_mysql_tag_ids** | **List[List[int]]** | Array of arrays of MySQL Tag Ids that specify db instances to Exclude. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**mysql_tag_ids** | **List[List[int]]** | Array of arrays of MySQL Tag Ids that specify db instances to Protect. | [optional] 
**objects** | [**List[AzureMySQLProtectionGroupObjectParams]**](AzureMySQLProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_my_sql_protection_group_params import AzureMySQLProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMySQLProtectionGroupParams from a JSON string
azure_my_sql_protection_group_params_instance = AzureMySQLProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureMySQLProtectionGroupParams.to_json())

# convert the object into a dict
azure_my_sql_protection_group_params_dict = azure_my_sql_protection_group_params_instance.to_dict()
# create an instance of AzureMySQLProtectionGroupParams from a dict
azure_my_sql_protection_group_params_from_dict = AzureMySQLProtectionGroupParams.from_dict(azure_my_sql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


