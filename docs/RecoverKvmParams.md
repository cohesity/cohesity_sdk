# RecoverKvmParams

Specifies the recovery options specific to KVM environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. | [optional] 
**recover_vm_params** | [**RecoverKvmVmParams**](RecoverKvmVmParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 

## Example

```python
from cohesity_sdk.models.recover_kvm_params import RecoverKvmParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmParams from a JSON string
recover_kvm_params_instance = RecoverKvmParams.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmParams.to_json())

# convert the object into a dict
recover_kvm_params_dict = recover_kvm_params_instance.to_dict()
# create an instance of RecoverKvmParams from a dict
recover_kvm_params_from_dict = RecoverKvmParams.from_dict(recover_kvm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


