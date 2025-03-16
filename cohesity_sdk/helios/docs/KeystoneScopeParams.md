# KeystoneScopeParams

Specifies scope paramteres of a Keystone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_scope_params** | [**DomainScopeParams**](DomainScopeParams.md) | Specifies the parameters for domain type scope. | [optional] 
**project_scope_params** | [**ProjectScopeParams**](ProjectScopeParams.md) | Specifies the parameter for project type scope. | [optional] 
**type** | **str** | Specifies the scope type. | 

## Example

```python
from cohesity_sdk.helios.models.keystone_scope_params import KeystoneScopeParams

# TODO update the JSON string below
json = "{}"
# create an instance of KeystoneScopeParams from a JSON string
keystone_scope_params_instance = KeystoneScopeParams.from_json(json)
# print the JSON string representation of the object
print(KeystoneScopeParams.to_json())

# convert the object into a dict
keystone_scope_params_dict = keystone_scope_params_instance.to_dict()
# create an instance of KeystoneScopeParams from a dict
keystone_scope_params_from_dict = KeystoneScopeParams.from_dict(keystone_scope_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


