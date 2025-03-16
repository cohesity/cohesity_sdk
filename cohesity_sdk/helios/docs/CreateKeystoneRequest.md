# CreateKeystoneRequest

Specifies the parameters to create a Keystone configuration.

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
from cohesity_sdk.helios.models.create_keystone_request import CreateKeystoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeystoneRequest from a JSON string
create_keystone_request_instance = CreateKeystoneRequest.from_json(json)
# print the JSON string representation of the object
print(CreateKeystoneRequest.to_json())

# convert the object into a dict
create_keystone_request_dict = create_keystone_request_instance.to_dict()
# create an instance of CreateKeystoneRequest from a dict
create_keystone_request_from_dict = CreateKeystoneRequest.from_dict(create_keystone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


