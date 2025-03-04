# OpenIdConnectAction

Open ID Connect Action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies an action to perform on an Open ID Connect Identity Provider. The following actions are currently supported: 1. &#39;RefreshPublicKeys&#39;: Refreshes the public keys currently stored on the cluster for the user sending the request. In order to do this, the public key URL specified in the current users Open ID configuration will be polled for a new public key. | 

## Example

```python
from cohesity_sdk.models.open_id_connect_action import OpenIdConnectAction

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectAction from a JSON string
open_id_connect_action_instance = OpenIdConnectAction.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectAction.to_json())

# convert the object into a dict
open_id_connect_action_dict = open_id_connect_action_instance.to_dict()
# create an instance of OpenIdConnectAction from a dict
open_id_connect_action_from_dict = OpenIdConnectAction.from_dict(open_id_connect_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


