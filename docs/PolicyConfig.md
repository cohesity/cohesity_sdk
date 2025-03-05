# PolicyConfig

Specifies the policy configuration for protecting an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[ObjectPolicy]**](ObjectPolicy.md) | Specifies the list of protection policies for protecting an object with multiple policies. | [optional] 

## Example

```python
from cohesity_sdk.models.policy_config import PolicyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyConfig from a JSON string
policy_config_instance = PolicyConfig.from_json(json)
# print the JSON string representation of the object
print(PolicyConfig.to_json())

# convert the object into a dict
policy_config_dict = policy_config_instance.to_dict()
# create an instance of PolicyConfig from a dict
policy_config_from_dict = PolicyConfig.from_dict(policy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


