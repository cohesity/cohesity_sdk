# AzureObjectProtectionResponseParams

Specifies the parameters which are specific to Azure related Object Protection response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the Azure Protection Job type. | [optional] 
**azure_sql_protection_type_params** | [**AzureSqlObjectProtectionParams**](AzureSqlObjectProtectionParams.md) |  | [optional] 
**native_protection_type_params** | [**AzureNativeObjectProtectionParams**](AzureNativeObjectProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_object_protection_response_params import AzureObjectProtectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureObjectProtectionResponseParams from a JSON string
azure_object_protection_response_params_instance = AzureObjectProtectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(AzureObjectProtectionResponseParams.to_json())

# convert the object into a dict
azure_object_protection_response_params_dict = azure_object_protection_response_params_instance.to_dict()
# create an instance of AzureObjectProtectionResponseParams from a dict
azure_object_protection_response_params_from_dict = AzureObjectProtectionResponseParams.from_dict(azure_object_protection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


