# RecoverVmwareParams

Specifies the recovery options specific to VMware environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) | Specifies the parameters to download files and folders. | [optional] 
**mount_volume_params** | [**MountVmwareVolumeParams**](MountVmwareVolumeParams.md) | Specifies the parameters to mount VMware Volumes. | [optional] 
**objects** | [**List[RecoverVmwareSnapshotParams]**](RecoverVmwareSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_file_and_folder_params** | [**RecoverVMwareFileAndFolderParams**](RecoverVMwareFileAndFolderParams.md) | Specifies the parameters to recover files and folders. | [optional] 
**recover_v_app_params** | [**RecoverVmwareVAppParams**](RecoverVmwareVAppParams.md) | Specifies the parameters to recover a VMware vApp. | [optional] 
**recover_v_app_template_params** | [**RecoverVmwareVAppTemplateParams**](RecoverVmwareVAppTemplateParams.md) | Specifies the parameters to recover a VMware vApp template. | [optional] 
**recover_vm_disk_params** | [**RecoverVmwareDiskParams**](RecoverVmwareDiskParams.md) | Specifies the parameters to recover VMware Disks. | [optional] 
**recover_vm_params** | [**RecoverVmwareVmParams**](RecoverVmwareVmParams.md) | Specifies the parameters to recover VMware VM. | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_params import RecoverVmwareParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareParams from a JSON string
recover_vmware_params_instance = RecoverVmwareParams.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareParams.to_json())

# convert the object into a dict
recover_vmware_params_dict = recover_vmware_params_instance.to_dict()
# create an instance of RecoverVmwareParams from a dict
recover_vmware_params_from_dict = RecoverVmwareParams.from_dict(recover_vmware_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


