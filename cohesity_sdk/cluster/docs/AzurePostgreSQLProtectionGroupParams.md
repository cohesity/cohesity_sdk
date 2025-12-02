# AzurePostgreSQLProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure PostgreSQL workload. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_postgresql_tag_ids** | **List[List[int]]** | Array of arrays of PostgreSQL Tag Ids that specify db instances to Exclude. | [optional] 
**objects** | [**List[AzurePostgreSQLProtectionGroupObjectParams]**](AzurePostgreSQLProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**postgresql_tag_ids** | **List[List[int]]** | Array of arrays of PostgreSQL Tag Ids that specify db instances to Protect. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_postgre_sql_protection_group_params import AzurePostgreSQLProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePostgreSQLProtectionGroupParams from a JSON string
azure_postgre_sql_protection_group_params_instance = AzurePostgreSQLProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzurePostgreSQLProtectionGroupParams.to_json())

# convert the object into a dict
azure_postgre_sql_protection_group_params_dict = azure_postgre_sql_protection_group_params_instance.to_dict()
# create an instance of AzurePostgreSQLProtectionGroupParams from a dict
azure_postgre_sql_protection_group_params_from_dict = AzurePostgreSQLProtectionGroupParams.from_dict(azure_postgre_sql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


