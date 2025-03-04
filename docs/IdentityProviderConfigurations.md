# IdentityProviderConfigurations

Identity provider configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idps** | [**List[IdentityProviderConfiguration]**](IdentityProviderConfiguration.md) | Specifies a list of identity provider configurations | [optional] 

## Example

```python
from cohesity_sdk.models.identity_provider_configurations import IdentityProviderConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderConfigurations from a JSON string
identity_provider_configurations_instance = IdentityProviderConfigurations.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderConfigurations.to_json())

# convert the object into a dict
identity_provider_configurations_dict = identity_provider_configurations_instance.to_dict()
# create an instance of IdentityProviderConfigurations from a dict
identity_provider_configurations_from_dict = IdentityProviderConfigurations.from_dict(identity_provider_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


