# KeystoneCredentials

Specifies user credentials of a Keystone server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_creds** | [**KeystoneAdminParams**](KeystoneAdminParams.md) | Specifies parameters related to Keystone administrator. | 
**scope** | [**KeystoneScopeParams**](KeystoneScopeParams.md) | Specifies parameters related to Keystone scope. | 

## Example

```python
from cohesity_sdk.helios.models.keystone_credentials import KeystoneCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of KeystoneCredentials from a JSON string
keystone_credentials_instance = KeystoneCredentials.from_json(json)
# print the JSON string representation of the object
print(KeystoneCredentials.to_json())

# convert the object into a dict
keystone_credentials_dict = keystone_credentials_instance.to_dict()
# create an instance of KeystoneCredentials from a dict
keystone_credentials_from_dict = KeystoneCredentials.from_dict(keystone_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


