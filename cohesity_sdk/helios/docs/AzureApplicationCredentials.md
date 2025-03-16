# AzureApplicationCredentials

Specifies the credentials of an application from Azure active directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Specifies the application id of an Azure active directory application. | 
**application_object_id** | **str** | Specifies the application object id of an Azure active directory application. | [optional] 
**encrypted_application_key** | **str** | Specifies the encrypted application key of an Azure active directory application. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_application_credentials import AzureApplicationCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AzureApplicationCredentials from a JSON string
azure_application_credentials_instance = AzureApplicationCredentials.from_json(json)
# print the JSON string representation of the object
print(AzureApplicationCredentials.to_json())

# convert the object into a dict
azure_application_credentials_dict = azure_application_credentials_instance.to_dict()
# create an instance of AzureApplicationCredentials from a dict
azure_application_credentials_from_dict = AzureApplicationCredentials.from_dict(azure_application_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


