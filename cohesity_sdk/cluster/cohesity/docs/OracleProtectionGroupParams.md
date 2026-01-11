# OracleProtectionGroupParams

Specifies the parameters to create Oracle Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[OracleProtectionGroupObjectParams], none_type**](OracleProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 
**full_auto_kill_timeout_secs** | **int, none_type** | Time in seconds after which the full backup of the database in given backup job should be auto-killed. | [optional] 
**incr_auto_kill_timeout_secs** | **int, none_type** | Time in seconds after which the incremental backup of the database in given backup job should be auto-killed. | [optional] 
**log_auto_kill_timeout_secs** | **int, none_type** | Time in seconds after which the log backup of the database in given backup job should be auto-killed. | [optional] 
**nfs_protocol** | **str, none_type** | Specifies the preferred protocol to use if this device supports multiple protocols. | [optional] 
**persist_mountpoints** | **bool, none_type** | Specifies whether the mountpoints created while backing up Oracle DBs should be persisted. Defaults to true if value is null to handle the backward compatibility for the upgrade case. | [optional]  if omitted the server will use the default value of True
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


