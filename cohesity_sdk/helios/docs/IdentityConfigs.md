# IdentityConfigs

Identity Provider Configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idps** | [**List[IdentityConfig]**](IdentityConfig.md) | Specifies a list of Identity Providers. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.identity_configs import IdentityConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityConfigs from a JSON string
identity_configs_instance = IdentityConfigs.from_json(json)
# print the JSON string representation of the object
print(IdentityConfigs.to_json())

# convert the object into a dict
identity_configs_dict = identity_configs_instance.to_dict()
# create an instance of IdentityConfigs from a dict
identity_configs_from_dict = IdentityConfigs.from_dict(identity_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


