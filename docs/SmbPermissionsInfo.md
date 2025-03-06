# SmbPermissionsInfo

Specifies information about SMB permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_sid** | **str** | Specifies the security identifier (SID) of the owner of the SMB share. | [optional] 
**permissions** | [**List[SmbPermission]**](SmbPermission.md) | Array of SMB Permissions. Specifies a list of SMB permissions. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.smb_permissions_info import SmbPermissionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SmbPermissionsInfo from a JSON string
smb_permissions_info_instance = SmbPermissionsInfo.from_json(json)
# print the JSON string representation of the object
print(SmbPermissionsInfo.to_json())

# convert the object into a dict
smb_permissions_info_dict = smb_permissions_info_instance.to_dict()
# create an instance of SmbPermissionsInfo from a dict
smb_permissions_info_from_dict = SmbPermissionsInfo.from_dict(smb_permissions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


