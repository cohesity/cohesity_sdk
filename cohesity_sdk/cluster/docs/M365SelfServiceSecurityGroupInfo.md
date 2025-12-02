# M365SelfServiceSecurityGroupInfo

Specifies the Security Group Information for Self-Service Configuration. The member users of this Security Group will have the Self-Service workflow enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_download** | **bool** | Specifies whether the Security Group members are allowed to download content of their Mailbox or OneDrive. | [optional] 
**global_id** | **str** | Specifies the Global ID of this Security Group | 
**name** | **str** | Specifies the name of the Security Group | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.m365_self_service_security_group_info import M365SelfServiceSecurityGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of M365SelfServiceSecurityGroupInfo from a JSON string
m365_self_service_security_group_info_instance = M365SelfServiceSecurityGroupInfo.from_json(json)
# print the JSON string representation of the object
print(M365SelfServiceSecurityGroupInfo.to_json())

# convert the object into a dict
m365_self_service_security_group_info_dict = m365_self_service_security_group_info_instance.to_dict()
# create an instance of M365SelfServiceSecurityGroupInfo from a dict
m365_self_service_security_group_info_from_dict = M365SelfServiceSecurityGroupInfo.from_dict(m365_self_service_security_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


