# KeystoneAdminParams

Specifies administrator credentials of a Keystone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the administrator domain name. | 
**password** | **str** | Specifies the password of Keystone administrator. | [optional] 
**username** | **str** | Specifies the username of Keystone administrator. | 

## Example

```python
from cohesity_sdk.models.keystone_admin_params import KeystoneAdminParams

# TODO update the JSON string below
json = "{}"
# create an instance of KeystoneAdminParams from a JSON string
keystone_admin_params_instance = KeystoneAdminParams.from_json(json)
# print the JSON string representation of the object
print(KeystoneAdminParams.to_json())

# convert the object into a dict
keystone_admin_params_dict = keystone_admin_params_instance.to_dict()
# create an instance of KeystoneAdminParams from a dict
keystone_admin_params_from_dict = KeystoneAdminParams.from_dict(keystone_admin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


