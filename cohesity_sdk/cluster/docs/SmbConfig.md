# SmbConfig

Specifies the SMB config settings for this View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_fast_durable_handle** | **bool** | Specifies whether fast durable handle is enabled. If enabled, view open handle will be kept in memory, which results in a higher performance. But the handles cannot be recovered if node or service crashes. | [optional] 
**enable_smb_access_based_enumeration** | **bool** | Specifies if access-based enumeration should be enabled. If &#39;true&#39;, only files and folders that the user has permissions to access are visible on the SMB share for that user. | [optional] 
**enable_smb_encryption** | **bool** | Specifies the SMB encryption for the View. If set, it enables the SMB encryption for the View. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format. | [optional] 
**enable_smb_oplock** | **bool** | Specifies whether SMB opportunistic lock is enabled. | [optional] 
**enable_smb_view_discovery** | **bool** | If set, it enables discovery of view for SMB. | [optional] 
**enforce_smb_encryption** | **bool** | Specifies the SMB encryption for all the sessions for the View. If set, encryption is enforced for all the sessions for the View. When enabled all future and existing unencrypted sessions are disallowed. | [optional] 
**share_permissions** | [**ViewSharePermissions**](ViewSharePermissions.md) |  | [optional] 
**smb_permissions_info** | [**SmbPermissionsInfo**](SmbPermissionsInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.smb_config import SmbConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SmbConfig from a JSON string
smb_config_instance = SmbConfig.from_json(json)
# print the JSON string representation of the object
print(SmbConfig.to_json())

# convert the object into a dict
smb_config_dict = smb_config_instance.to_dict()
# create an instance of SmbConfig from a dict
smb_config_from_dict = SmbConfig.from_dict(smb_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


