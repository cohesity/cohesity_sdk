# AzureNativeObjectProtectionParams

Specifies the parameters which are specific to Azure Object Protection Groups using Azure native APIs. Atlease one of tags or objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_transfer_info** | [**DataTransferInfo**](DataTransferInfo.md) |  | [optional] 
**objects** | [**List[AzureObjectLevelParams]**](AzureObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_native_object_protection_params import AzureNativeObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureNativeObjectProtectionParams from a JSON string
azure_native_object_protection_params_instance = AzureNativeObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AzureNativeObjectProtectionParams.to_json())

# convert the object into a dict
azure_native_object_protection_params_dict = azure_native_object_protection_params_instance.to_dict()
# create an instance of AzureNativeObjectProtectionParams from a dict
azure_native_object_protection_params_from_dict = AzureNativeObjectProtectionParams.from_dict(azure_native_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


