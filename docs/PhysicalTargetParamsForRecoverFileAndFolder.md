# PhysicalTargetParamsForRecoverFileAndFolder

Specifies the parameters for a Physical recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_target** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the target entity where the volumes are being mounted. | 
**restore_to_original_paths** | **bool, none_type** | If this is true, then files will be restored to original paths. | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**alternate_restore_directory** | **str, none_type** | Specifies the directory path where restore should happen if restore_to_original_paths is set to false. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**preserve_timestamps** | **bool, none_type** | Whether to preserve the original time stamps. | [optional] 
**preserve_acls** | **bool, none_type** | Whether to preserve the ACLs of the original file. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other volumes if one of the volumes fails to recover. Default value is false. | [optional] 
**save_success_files** | **bool, none_type** | Specifies whether to save success files or not. Default value is false | [optional] 
**vlan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


