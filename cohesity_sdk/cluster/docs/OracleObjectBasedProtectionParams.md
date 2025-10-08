# OracleObjectBasedProtectionParams

Specifies the parameters specific to Oracle Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[OracleObjectProtectionInfo], none_type**](OracleObjectProtectionInfo.md) | Specifies the list of object ids to be protected. | 
**full_auto_kill_timeout_secs** | **int, none_type** | Time in seconds after which the full backup of the database in given backup job should be auto-killed. | [optional] 
**incr_auto_kill_timeout_secs** | **int, none_type** | Time in seconds after which the incremental backup of the database in given backup job should be auto-killed. | [optional] 
**log_auto_kill_timeout_secs** | **int, none_type** | Time in seconds after which the log backup of the database in given backup job should be auto-killed. | [optional] 
**persist_mountpoints** | **bool, none_type** | Specifies whether the mountpoints created while backing up Oracle DBs should be persisted.Defaults to true if value is null to handle the backward compatibility for the upgrade case. | [optional]  if omitted the server will use the default value of True
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


