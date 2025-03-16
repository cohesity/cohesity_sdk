# RecoverGcpParams

Specifies the recovery options specific to GCP environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) | Specifies the parameters to download files and folders. | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. | [optional] 
**recover_file_and_folder_params** | [**RecoverGcpFileAndFolderParams**](RecoverGcpFileAndFolderParams.md) | Specifies the parameters to recover files and folders. | [optional] 
**recover_vm_params** | [**RecoverGcpVmParams**](RecoverGcpVmParams.md) | Specifies the parameters to recover GCP VM. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.recover_gcp_params import RecoverGcpParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGcpParams from a JSON string
recover_gcp_params_instance = RecoverGcpParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGcpParams.to_json())

# convert the object into a dict
recover_gcp_params_dict = recover_gcp_params_instance.to_dict()
# create an instance of RecoverGcpParams from a dict
recover_gcp_params_from_dict = RecoverGcpParams.from_dict(recover_gcp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


