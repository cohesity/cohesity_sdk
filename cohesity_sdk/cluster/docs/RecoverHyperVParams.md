# RecoverHyperVParams

Specifies the recovery options specific to HyperV environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**mount_volume_params** | [**MountHyperVVolumeParams**](MountHyperVVolumeParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_file_and_folder_params** | [**RecoverHyperVFileAndFolderParams**](RecoverHyperVFileAndFolderParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverHyperVVmParams**](RecoverHyperVVmParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_hyper_v_params import RecoverHyperVParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVParams from a JSON string
recover_hyper_v_params_instance = RecoverHyperVParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVParams.to_json())

# convert the object into a dict
recover_hyper_v_params_dict = recover_hyper_v_params_instance.to_dict()
# create an instance of RecoverHyperVParams from a dict
recover_hyper_v_params_from_dict = RecoverHyperVParams.from_dict(recover_hyper_v_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


