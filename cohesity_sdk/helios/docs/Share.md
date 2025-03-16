# Share

Specifies the details of a Share.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_subnet_whitelist** | [**List[Subnet]**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 
**enable_filer_audit_logging** | **bool** | This field is currently deprecated. Specifies if Filer Audit Logging is enabled for this Share. | [optional] 
**file_audit_logging_state** | **str** | Specifies the state of File Audit logging for this Share. Inherited: Audit log setting is inherited from the  View. Enabled: Audit log is enabled for this Share. Disabled: Audit log is disabled for this Share. | [optional] 
**smb_config** | [**AliasSmbConfig**](AliasSmbConfig.md) | SMB config for the alias (share). | [optional] 
**name** | **str** | Specifies the Share name. | 
**nfs_mount_paths** | **List[str]** | Specifies the path for mounting this Share as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has its own path. | [optional] [readonly] 
**s3_access_path** | **str** | Specifies the path to access this Share as an S3 share. | [optional] [readonly] 
**smb_mount_paths** | **List[str]** | Specifies the possible paths that can be used to mount this Share as a SMB share. If Active Directory has multiple account names, each machine account has its own path. | [optional] [readonly] 
**tenant_id** | **str** | Specifies the tenant id who has access to this Share. | [optional] [readonly] 
**view_id** | **int** | Specifies the id of the View. | [optional] [readonly] 
**view_name** | **str** | Specifies the View name of this Share. | 
**view_path** | **str** | Specifies the View path of this Share. | 

## Example

```python
from cohesity_sdk.helios.models.share import Share

# TODO update the JSON string below
json = "{}"
# create an instance of Share from a JSON string
share_instance = Share.from_json(json)
# print the JSON string representation of the object
print(Share.to_json())

# convert the object into a dict
share_dict = share_instance.to_dict()
# create an instance of Share from a dict
share_from_dict = Share.from_dict(share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


