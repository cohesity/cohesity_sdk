# IdentityAction

Identity Action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_provider_type** | **str** | Specifies the type of identity provider the action will be performed on. | 
**o_auth2_params** | [**OAuth2Action**](OAuth2Action.md) |  | [optional] 
**open_id_connect_params** | [**OpenIdConnectAction**](OpenIdConnectAction.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.identity_action import IdentityAction

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAction from a JSON string
identity_action_instance = IdentityAction.from_json(json)
# print the JSON string representation of the object
print(IdentityAction.to_json())

# convert the object into a dict
identity_action_dict = identity_action_instance.to_dict()
# create an instance of IdentityAction from a dict
identity_action_from_dict = IdentityAction.from_dict(identity_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


