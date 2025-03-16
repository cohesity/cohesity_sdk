# AzureTargetParamsForRecoverFileAndFolder

Specifies the parameters for an Azure files and folders recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other files if one of the objects encounters an error. Default is false. | [optional] 
**new_target_config** | [**AzureRecoverFilesNewTargetConfig**](AzureRecoverFilesNewTargetConfig.md) | Specifies the configuration for recovering to a new target. | [optional] 
**original_target_config** | [**AzureRecoverFilesOriginalTargetConfig**](AzureRecoverFilesOriginalTargetConfig.md) | Specifies the configuration for recovering to the original target. | [optional] 
**overwrite_existing** | **bool** | Specifies whether to overwrite the existing files. Default is true. | [optional] 
**preserve_attributes** | **bool** | Specifies whether to preserve original file/folder attributes. Default is true. | [optional] 
**recover_to_original_target** | **bool** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) | Specifies VLAN Params associated with the recovered files and folders. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_target_params_for_recover_file_and_folder import AzureTargetParamsForRecoverFileAndFolder

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverFileAndFolder from a JSON string
azure_target_params_for_recover_file_and_folder_instance = AzureTargetParamsForRecoverFileAndFolder.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverFileAndFolder.to_json())

# convert the object into a dict
azure_target_params_for_recover_file_and_folder_dict = azure_target_params_for_recover_file_and_folder_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverFileAndFolder from a dict
azure_target_params_for_recover_file_and_folder_from_dict = AzureTargetParamsForRecoverFileAndFolder.from_dict(azure_target_params_for_recover_file_and_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


