# OAuth2Action

OAuth 2 Action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies an action to perform on an OAuth 2 Identity Provider. The following actions are currently supported: 1. &#39;RefreshPublicKeys&#39;: Refreshes the public keys currently stored on the cluster for the user sending the request. In order to do this, the public key URL specified in the current users OAuth configuration will be polled for a new public key. | 

## Example

```python
from cohesity_sdk.helios.models.o_auth2_action import OAuth2Action

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Action from a JSON string
o_auth2_action_instance = OAuth2Action.from_json(json)
# print the JSON string representation of the object
print(OAuth2Action.to_json())

# convert the object into a dict
o_auth2_action_dict = o_auth2_action_instance.to_dict()
# create an instance of OAuth2Action from a dict
o_auth2_action_from_dict = OAuth2Action.from_dict(o_auth2_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


