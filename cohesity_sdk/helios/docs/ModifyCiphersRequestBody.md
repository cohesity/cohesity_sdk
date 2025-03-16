# ModifyCiphersRequestBody

Specifies ciphers to enable/disable on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphers** | **List[str]** | Specifies a list of ciphers to enable/disable on the cluster. | 
**enable** | **bool** | If true, the ciphers passed in will be enabled on the cluster and all other ciphers will be disabled. If false, the ciphers specified will be disabled and all other ciphers on the cluster will be enabled. | 

## Example

```python
from cohesity_sdk.helios.models.modify_ciphers_request_body import ModifyCiphersRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyCiphersRequestBody from a JSON string
modify_ciphers_request_body_instance = ModifyCiphersRequestBody.from_json(json)
# print the JSON string representation of the object
print(ModifyCiphersRequestBody.to_json())

# convert the object into a dict
modify_ciphers_request_body_dict = modify_ciphers_request_body_instance.to_dict()
# create an instance of ModifyCiphersRequestBody from a dict
modify_ciphers_request_body_from_dict = ModifyCiphersRequestBody.from_dict(modify_ciphers_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


