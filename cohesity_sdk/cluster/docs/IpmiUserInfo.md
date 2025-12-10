# IpmiUserInfo

Specifies the ipmi user info for each node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_in** | **bool** | Specifies whether the user is allowed to initiate IPMI communication. | [optional] 
**id** | **int** | Specifies the id for the ipmi user. | [optional] 
**ipmi_msg** | **bool** | Specifies whether IPMI messaging is enabled for this user. | [optional] 
**link_auth** | **bool** | Specifies whether link-level authentication is required for this user. | [optional] 
**name** | **str** | Specifies the name of the ipmi user. | [optional] 
**privilege_level** | **int** | Specifies the privilege level assigned for this user. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_user_info import IpmiUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiUserInfo from a JSON string
ipmi_user_info_instance = IpmiUserInfo.from_json(json)
# print the JSON string representation of the object
print(IpmiUserInfo.to_json())

# convert the object into a dict
ipmi_user_info_dict = ipmi_user_info_instance.to_dict()
# create an instance of IpmiUserInfo from a dict
ipmi_user_info_from_dict = IpmiUserInfo.from_dict(ipmi_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


