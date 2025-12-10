# AzureMySQLProtectionGroupObjectParams

Specifies the object parameters to create Azure MySQL Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the azure source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_my_sql_protection_group_object_params import AzureMySQLProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMySQLProtectionGroupObjectParams from a JSON string
azure_my_sql_protection_group_object_params_instance = AzureMySQLProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AzureMySQLProtectionGroupObjectParams.to_json())

# convert the object into a dict
azure_my_sql_protection_group_object_params_dict = azure_my_sql_protection_group_object_params_instance.to_dict()
# create an instance of AzureMySQLProtectionGroupObjectParams from a dict
azure_my_sql_protection_group_object_params_from_dict = AzureMySQLProtectionGroupObjectParams.from_dict(azure_my_sql_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


