# RestoreVMwareVMParams

Specifies the parameters for a VMware recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_differential_restore** | **bool** | Specifies whether to attempt differential restore. | [optional] 
**datastore_ids** | **List[int]** | Specifies Datastore Ids, if the restore is to alternate location. | [optional] 
**enable_copy_recovery** | **bool** | Specifies whether to perform copy recovery or not. | [optional] 
**is_on_prem_deploy** | **bool** | Specifies whether a task in on prem deploy or not. | [optional] 
**overwrite_existing_vm** | **bool** | Specifies whether to overwrite the VM at the target location. | [optional] 
**power_off_and_rename_existing_vm** | **bool** | Specifies whether to power off and mark the VM at the target location as deprecated. | [optional] 
**resource_pool_id** | **int** | Specifies if the restore is to alternate location. | [optional] 
**target_data_store_id** | **int** | Specifies the folder where the restore datastore should be created. | [optional] 
**target_vm_folder_id** | **int** | Specifies the folder ID where the VMs should be created. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.restore_v_mware_vm_params import RestoreVMwareVMParams

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreVMwareVMParams from a JSON string
restore_v_mware_vm_params_instance = RestoreVMwareVMParams.from_json(json)
# print the JSON string representation of the object
print(RestoreVMwareVMParams.to_json())

# convert the object into a dict
restore_v_mware_vm_params_dict = restore_v_mware_vm_params_instance.to_dict()
# create an instance of RestoreVMwareVMParams from a dict
restore_v_mware_vm_params_from_dict = RestoreVMwareVMParams.from_dict(restore_v_mware_vm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


