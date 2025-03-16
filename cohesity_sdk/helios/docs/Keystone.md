# Keystone

Specifies a Keystone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_creds** | [**KeystoneAdminParams**](KeystoneAdminParams.md) | Specifies parameters related to Keystone administrator. | 
**scope** | [**KeystoneScopeParams**](KeystoneScopeParams.md) | Specifies parameters related to Keystone scope. | 
**auth_url** | **str** | Specifies the url points to the Keystone service. | 
**id** | **int** | Specifies the Keystone configuration id. | [optional] [readonly] 
**name** | **str** | Specifies the Keystone configuration name. | 

## Example

```python
from cohesity_sdk.helios.models.keystone import Keystone

# TODO update the JSON string below
json = "{}"
# create an instance of Keystone from a JSON string
keystone_instance = Keystone.from_json(json)
# print the JSON string representation of the object
print(Keystone.to_json())

# convert the object into a dict
keystone_dict = keystone_instance.to_dict()
# create an instance of Keystone from a dict
keystone_from_dict = Keystone.from_dict(keystone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


