# IpmiUsers

Specifies the list of IPMI users for the given node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Specifies the channel through which the IPMI interface communicates on the network. | [optional] 
**max_user_id** | **int** | Specifies the highest occupied ID up to which no free user IDs are available. If a new user is created, it is assigned a user ID of maxUserId + 1. | [optional] 
**user_list** | [**List[IpmiUserInfo]**](IpmiUserInfo.md) | Specifies the list of ipmi users with their permissions. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_users import IpmiUsers

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiUsers from a JSON string
ipmi_users_instance = IpmiUsers.from_json(json)
# print the JSON string representation of the object
print(IpmiUsers.to_json())

# convert the object into a dict
ipmi_users_dict = ipmi_users_instance.to_dict()
# create an instance of IpmiUsers from a dict
ipmi_users_from_dict = IpmiUsers.from_dict(ipmi_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


