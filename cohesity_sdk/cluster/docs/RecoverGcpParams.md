# RecoverGcpParams

Specifies the recovery options specific to GCP environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | defaults to "RecoverVMs"
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. | [optional] 
**recover_vm_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to recover GCP VM. | [optional] 
**download_file_and_folder_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to download files and folders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


