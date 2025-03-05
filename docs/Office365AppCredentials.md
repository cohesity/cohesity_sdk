# Office365AppCredentials

Specifies credentials for office365 azure registered applications, used for office 365 source registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the application ID that the registration portal (apps.dev.microsoft.com) assigned. | [optional] 
**client_secret** | **str** | Specifies the application secret that was created in app registration portal. | [optional] 

## Example

```python
from cohesity_sdk.models.office365_app_credentials import Office365AppCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of Office365AppCredentials from a JSON string
office365_app_credentials_instance = Office365AppCredentials.from_json(json)
# print the JSON string representation of the object
print(Office365AppCredentials.to_json())

# convert the object into a dict
office365_app_credentials_dict = office365_app_credentials_instance.to_dict()
# create an instance of Office365AppCredentials from a dict
office365_app_credentials_from_dict = Office365AppCredentials.from_dict(office365_app_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


