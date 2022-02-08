# GcpTargetParamsForRecoverFileAndFolder

Specifies the parameters for a GCP recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_vm** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the target VM to recover files and folders to. | 
**recover_to_original_paths** | **bool, none_type** | Specifies whether to recover files to original places. | 
**target_vm_credentials** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies credentials to access the target VM. | 
**alternate_base_directory** | **str, none_type** | Specifies a base directory under which all files and folders will be recovered. This is required if recoverToOriginalPaths is set to false. | [optional] 
**overwrite_originals** | **bool, none_type** | Specifies whether to override the existing files. Default is true. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve original attributes. Default is true. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other files if one of files or folders failed to recover. Default value is false. | [optional] 
**vlan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies VLAN Params associated with the recovered files and folders. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


