# ShareAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the Share name. | 
**view_name** | **str, none_type** | Specifies the View name of this Share. | 
**view_path** | **str, none_type** | Specifies the View path of this Share. | 
**nfs_mount_paths** | **[str], none_type** | Specifies the path for mounting this Share as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has its own path. | [optional] [readonly] 
**s3_access_path** | **str, none_type** | Specifies the path to access this Share as an S3 share. | [optional] [readonly] 
**smb_mount_paths** | **[str], none_type** | Specifies the possible paths that can be used to mount this Share as a SMB share. If Active Directory has multiple account names, each machine account has its own path. | [optional] [readonly] 
**tenant_id** | **str, none_type** | Specifies the tenant id who has access to this Share. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


