# RecoverAzureParams

Specifies the recovery options specific to Azure environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_sql_params** | [**RecoverAzureSqlParams**](RecoverAzureSqlParams.md) |  | [optional] 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_file_and_folder_params** | [**RecoverAzureFileAndFolderParams**](RecoverAzureFileAndFolderParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverAzureVmParams**](RecoverAzureVmParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.models.recover_azure_params import RecoverAzureParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureParams from a JSON string
recover_azure_params_instance = RecoverAzureParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureParams.to_json())

# convert the object into a dict
recover_azure_params_dict = recover_azure_params_instance.to_dict()
# create an instance of RecoverAzureParams from a dict
recover_azure_params_from_dict = RecoverAzureParams.from_dict(recover_azure_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


