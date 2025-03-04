# RegisterSwiftParams

Specifies the parameters to register a Swift service on Keystone server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keystone_credentials** | [**KeystoneCredentials**](KeystoneCredentials.md) |  | [optional] 
**tenant_id** | **str** | Specifies the tenant Id who&#39;s Swift service will be registered. | 

## Example

```python
from cohesity_sdk.models.register_swift_params import RegisterSwiftParams

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterSwiftParams from a JSON string
register_swift_params_instance = RegisterSwiftParams.from_json(json)
# print the JSON string representation of the object
print(RegisterSwiftParams.to_json())

# convert the object into a dict
register_swift_params_dict = register_swift_params_instance.to_dict()
# create an instance of RegisterSwiftParams from a dict
register_swift_params_from_dict = RegisterSwiftParams.from_dict(register_swift_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


