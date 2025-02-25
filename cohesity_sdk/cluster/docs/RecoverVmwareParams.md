# RecoverVmwareParams

Specifies the recovery options specific to VMware environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**mount_volume_params** | [**MountVmwareVolumeParams**](MountVmwareVolumeParams.md) |  | [optional] 
**objects** | [**[RecoverVmwareSnapshotParams], none_type**](RecoverVmwareSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_file_and_folder_params** | [**RecoverVMwareFileAndFolderParams**](RecoverVMwareFileAndFolderParams.md) |  | [optional] 
**recover_v_app_params** | [**RecoverVmwareVAppParams**](RecoverVmwareVAppParams.md) |  | [optional] 
**recover_v_app_template_params** | [**RecoverVmwareVAppTemplateParams**](RecoverVmwareVAppTemplateParams.md) |  | [optional] 
**recover_vm_disk_params** | [**RecoverVmwareDiskParams**](RecoverVmwareDiskParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverVmwareVmParams**](RecoverVmwareVmParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


