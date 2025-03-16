# FilerAuditLogConfigs

Specifies the filer audit log configs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfs_mount_path** | **str** | This field is currently deprecated. Please use NFS MountPaths which would be an array of strings. | [optional] [readonly] 
**nfs_mount_paths** | **List[str]** | Specifies a list of NFS mount paths of a Cohesity View containing filer audit logs. | [optional] [readonly] 
**override_global_subnet_whitelist** | **bool** | Specifies whether view level client subnet whitelist overrides cluster and global setting. | [optional] 
**share_permissions** | [**List[SmbPermission]**](SmbPermission.md) | Specifies a list of share level permissions. | [optional] 
**smb_mount_paths** | **List[str]** | Specifies a list of SMB mount paths of a Cohesity View containing filer audit logs. | [optional] [readonly] 
**subnet_whitelist** | [**List[Subnet]**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access a Cohesity View containing filer audit logs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.filer_audit_log_configs import FilerAuditLogConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of FilerAuditLogConfigs from a JSON string
filer_audit_log_configs_instance = FilerAuditLogConfigs.from_json(json)
# print the JSON string representation of the object
print(FilerAuditLogConfigs.to_json())

# convert the object into a dict
filer_audit_log_configs_dict = filer_audit_log_configs_instance.to_dict()
# create an instance of FilerAuditLogConfigs from a dict
filer_audit_log_configs_from_dict = FilerAuditLogConfigs.from_dict(filer_audit_log_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


