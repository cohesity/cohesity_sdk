# AzureCommonObjectProtectionParams

Specifies the parameters which are specific to Azure related Object Protection and common to different Azure protection types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the Azure Protection Job type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_common_object_protection_params import AzureCommonObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCommonObjectProtectionParams from a JSON string
azure_common_object_protection_params_instance = AzureCommonObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AzureCommonObjectProtectionParams.to_json())

# convert the object into a dict
azure_common_object_protection_params_dict = azure_common_object_protection_params_instance.to_dict()
# create an instance of AzureCommonObjectProtectionParams from a dict
azure_common_object_protection_params_from_dict = AzureCommonObjectProtectionParams.from_dict(azure_common_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


