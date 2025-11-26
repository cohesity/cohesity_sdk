# HyperVTargetParamsForRecoverFileAndFolder

Specifies the parameters for a HyperV recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_original_target** | **bool, none_type** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other files if one of files or folders failed to recover. Default value is false. | [optional] 
**new_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the configuration for recovering to a new target. | [optional] 
**original_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the configuration for recovering to the original target. | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to override the existing files. Default is true. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve original attributes. Default is true. | [optional] 
**vlan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies VLAN Params associated with the recovered files and folders. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


