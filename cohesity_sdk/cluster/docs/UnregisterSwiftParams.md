# UnregisterSwiftParams

Specifies the parameters to unregister a Swift service from Keystone server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keystone_credentials** | [**KeystoneCredentials**](KeystoneCredentials.md) |  | [optional] 
**tenant_id** | **str** | Specifies the tenant Id who&#39;s Swift service will be unregistered. | 

## Example

```python
from cohesity_sdk.cluster.models.unregister_swift_params import UnregisterSwiftParams

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterSwiftParams from a JSON string
unregister_swift_params_instance = UnregisterSwiftParams.from_json(json)
# print the JSON string representation of the object
print(UnregisterSwiftParams.to_json())

# convert the object into a dict
unregister_swift_params_dict = unregister_swift_params_instance.to_dict()
# create an instance of UnregisterSwiftParams from a dict
unregister_swift_params_from_dict = UnregisterSwiftParams.from_dict(unregister_swift_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


