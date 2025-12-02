# AzureCredentials

Specifies the object to Azure related credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Specifies the type of authentication being used in the request. | 
**managed_identity_client_id** | **str** | Specifies the Managed Identity&#39;s client id associated with the Virtual Machine using which actions can be performed. It&#39;s applicable only when user selects User Managed Identity auth method. | [optional] 
**password** | **str** | Specifies the password to access target entity. | [optional] 
**username** | **str** | Specifies the username to access target entity. Required for UserPassword auth type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_credentials import AzureCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCredentials from a JSON string
azure_credentials_instance = AzureCredentials.from_json(json)
# print the JSON string representation of the object
print(AzureCredentials.to_json())

# convert the object into a dict
azure_credentials_dict = azure_credentials_instance.to_dict()
# create an instance of AzureCredentials from a dict
azure_credentials_from_dict = AzureCredentials.from_dict(azure_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


