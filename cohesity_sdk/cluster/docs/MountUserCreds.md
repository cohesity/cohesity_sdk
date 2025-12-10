# MountUserCreds

Specify creds for mounting SMB share on the host

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain the user belongs to. Optional domain if a user from AD is selected. | [optional] 
**is_local_user** | **bool** | Specifies if the selected user is local user which is created on the cluster or a domain user | 
**password** | **str** | Specifies the password to access the SMB share. Optional if domain user is selected. | [optional] 
**sid** | **str** | Specifies the SID of the user selected. This should be in the correct format and should be referring the username passed. If passed wrongly then restore will fail. | 
**username** | **str** | Specifies the username to mount the SMB share. The specified user would only have the SMB access to the cloned view. | 

## Example

```python
from cohesity_sdk.cluster.models.mount_user_creds import MountUserCreds

# TODO update the JSON string below
json = "{}"
# create an instance of MountUserCreds from a JSON string
mount_user_creds_instance = MountUserCreds.from_json(json)
# print the JSON string representation of the object
print(MountUserCreds.to_json())

# convert the object into a dict
mount_user_creds_dict = mount_user_creds_instance.to_dict()
# create an instance of MountUserCreds from a dict
mount_user_creds_from_dict = MountUserCreds.from_dict(mount_user_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


