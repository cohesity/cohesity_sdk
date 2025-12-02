# AzureSQLMIProtectionGroupObjectParams

Specifies the object parameters to create Azure SQL MI Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the azure source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_sqlmi_protection_group_object_params import AzureSQLMIProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSQLMIProtectionGroupObjectParams from a JSON string
azure_sqlmi_protection_group_object_params_instance = AzureSQLMIProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AzureSQLMIProtectionGroupObjectParams.to_json())

# convert the object into a dict
azure_sqlmi_protection_group_object_params_dict = azure_sqlmi_protection_group_object_params_instance.to_dict()
# create an instance of AzureSQLMIProtectionGroupObjectParams from a dict
azure_sqlmi_protection_group_object_params_from_dict = AzureSQLMIProtectionGroupObjectParams.from_dict(azure_sqlmi_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


