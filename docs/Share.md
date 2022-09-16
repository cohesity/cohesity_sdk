# Share

Specifies the details of a Share.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the Share name. | 
**view_name** | **str, none_type** | Specifies the View name of this Share. | 
**view_path** | **str, none_type** | Specifies the View path of this Share. | 
**enable_filer_audit_logging** | **bool, none_type** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**smb_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | SMB config for the alias (share). | [optional] 
**client_subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 
**nfs_mount_paths** | **[str], none_type** | Specifies the path for mounting this Share as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has its own path. | [optional] [readonly] 
**smb_mount_paths** | **[str], none_type** | Specifies the possible paths that can be used to mount this Share as a SMB share. If Active Directory has multiple account names, each machine account has its own path. | [optional] [readonly] 
**s3_access_path** | **str, none_type** | Specifies the path to access this Share as an S3 share. | [optional] [readonly] 
**tenant_id** | **str, none_type** | Specifies the tenant id who has access to this Share. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


