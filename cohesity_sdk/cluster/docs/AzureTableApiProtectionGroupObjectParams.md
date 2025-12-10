# AzureTableApiProtectionGroupObjectParams

Specifies the object parameters to create Azure Table API Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the azure source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_table_api_protection_group_object_params import AzureTableApiProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTableApiProtectionGroupObjectParams from a JSON string
azure_table_api_protection_group_object_params_instance = AzureTableApiProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AzureTableApiProtectionGroupObjectParams.to_json())

# convert the object into a dict
azure_table_api_protection_group_object_params_dict = azure_table_api_protection_group_object_params_instance.to_dict()
# create an instance of AzureTableApiProtectionGroupObjectParams from a dict
azure_table_api_protection_group_object_params_from_dict = AzureTableApiProtectionGroupObjectParams.from_dict(azure_table_api_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


