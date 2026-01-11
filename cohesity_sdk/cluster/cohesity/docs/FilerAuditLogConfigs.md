# FilerAuditLogConfigs

Specifies the filer audit log configs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfs_mount_path** | **str, none_type** | This field is currently deprecated. Please use NFS MountPaths which would be an array of strings. | [optional] [readonly] 
**nfs_mount_paths** | **[str], none_type** | Specifies a list of NFS mount paths of a Cohesity View containing filer audit logs. | [optional] [readonly] 
**override_global_subnet_whitelist** | **bool, none_type** | Specifies whether view level client subnet whitelist overrides cluster and global setting. | [optional] 
**share_permissions** | [**[SmbPermission], none_type**](SmbPermission.md) | Specifies a list of share level permissions. | [optional] 
**smb_mount_paths** | **[str], none_type** | Specifies a list of SMB mount paths of a Cohesity View containing filer audit logs. | [optional] [readonly] 
**subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access a Cohesity View containing filer audit logs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


