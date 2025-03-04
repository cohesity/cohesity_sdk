# SupportUserConfig

Specifies the support user's configuration on the Cohesity cluster such as if its shell password has been set and/or sudo access is granted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_sudo_access** | **bool** | Specifies if the support user has sudo access. | [optional] 
**password_set** | **bool** | Specifies if the password for the support user has been set. | [optional] 

## Example

```python
from cohesity_sdk.models.support_user_config import SupportUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SupportUserConfig from a JSON string
support_user_config_instance = SupportUserConfig.from_json(json)
# print the JSON string representation of the object
print(SupportUserConfig.to_json())

# convert the object into a dict
support_user_config_dict = support_user_config_instance.to_dict()
# create an instance of SupportUserConfig from a dict
support_user_config_from_dict = SupportUserConfig.from_dict(support_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


