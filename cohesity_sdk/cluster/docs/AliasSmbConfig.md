# AliasSmbConfig

Message defining SMB config for IRIS. SMB config contains SMB encryption flags, SMB discoverable flag and Share level permissions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching_enabled** | **bool, none_type** | Indicate if offline file caching is supported. | [optional] 
**continuous_availability** | **bool, none_type** | Whether file open handles are persisted to scribe to survive bridge process crash. When set to false, open handles will be kept in memory until the current node has exclusive ticket for the entity handle. When the entity is opened from another node, the exclusive ticket would be revoked from the node. In revoke control flow, the current node would persist the state to scribe. On acquiring the exclusive ticket,another node would read the file open handles from scribe and resume the handling of operation. | [optional] 
**discovery_enabled** | **bool, none_type** | Whether the share is discoverable. | [optional] 
**encryption_enabled** | **bool, none_type** | Whether SMB encryption is enabled for this share. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format. | [optional] 
**encryption_required** | **bool, none_type** | Whether to enforce encryption for all the sessions for this view. When enabled all unencrypted sessions are disallowed. | [optional] 
**is_share_level_permission_empty** | **bool, none_type** | Indicate if share level permission is cleared by user. | [optional] 
**oplock_enabled** | **bool, none_type** | Indicate the operation lock is enabled by this view. | [optional] 
**permissions** | [**[SmbPermission], none_type**](SmbPermission.md) | Share level permissions. Note: Supported Access: FullControl, Modify, ReadOnly. Supported type: Allow, Deny. | [optional] 
**super_user_sids** | **[str], none_type** | Specifies a list of super user sids. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


