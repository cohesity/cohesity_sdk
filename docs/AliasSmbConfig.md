# AliasSmbConfig

Message defining SMB config for IRIS. SMB config contains SMB encryption flags, SMB discoverable flag and Share level permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching_enabled** | **bool** | Indicate if offline file caching is supported. | [optional] 
**continuous_availability** | **bool** | Whether file open handles are persisted to scribe to survive bridge process crash. When set to false, open handles will be kept in memory until the current node has exclusive ticket for the entity handle. When the entity is opened from another node, the exclusive ticket would be revoked from the node. In revoke control flow, the current node would persist the state to scribe. On acquiring the exclusive ticket,another node would read the file open handles from scribe and resume the handling of operation. | [optional] 
**discovery_enabled** | **bool** | Whether the share is discoverable. | [optional] 
**encryption_enabled** | **bool** | Whether SMB encryption is enabled for this share. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format. | [optional] 
**encryption_required** | **bool** | Whether to enforce encryption for all the sessions for this view. When enabled all unencrypted sessions are disallowed. | [optional] 
**is_share_level_permission_empty** | **bool** | Indicate if share level permission is cleared by user. | [optional] 
**oplock_enabled** | **bool** | Indicate the operation lock is enabled by this view. | [optional] 
**permissions** | [**List[SmbPermission]**](SmbPermission.md) | Share level permissions. Note: Supported Access: FullControl, Modify, ReadOnly. Supported type: Allow, Deny. | [optional] 
**super_user_sids** | **List[str]** | Specifies a list of super user sids. | [optional] 

## Example

```python
from cohesity_sdk.models.alias_smb_config import AliasSmbConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AliasSmbConfig from a JSON string
alias_smb_config_instance = AliasSmbConfig.from_json(json)
# print the JSON string representation of the object
print(AliasSmbConfig.to_json())

# convert the object into a dict
alias_smb_config_dict = alias_smb_config_instance.to_dict()
# create an instance of AliasSmbConfig from a dict
alias_smb_config_from_dict = AliasSmbConfig.from_dict(alias_smb_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


