# AzureObjectProtectionRequestParams

Specifies the parameters which are specific to Azure related Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the Azure Protection Job type. | [optional] 
**azure_sql_protection_type_params** | [**AzureSqlObjectProtectionParams**](AzureSqlObjectProtectionParams.md) |  | [optional] 
**native_protection_type_params** | [**AzureNativeObjectProtectionParams**](AzureNativeObjectProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_object_protection_request_params import AzureObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureObjectProtectionRequestParams from a JSON string
azure_object_protection_request_params_instance = AzureObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(AzureObjectProtectionRequestParams.to_json())

# convert the object into a dict
azure_object_protection_request_params_dict = azure_object_protection_request_params_instance.to_dict()
# create an instance of AzureObjectProtectionRequestParams from a dict
azure_object_protection_request_params_from_dict = AzureObjectProtectionRequestParams.from_dict(azure_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


