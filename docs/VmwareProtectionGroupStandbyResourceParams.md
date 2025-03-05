# VmwareProtectionGroupStandbyResourceParams

VMware protection group standby resource params which will be used to create standby VM entity for backup entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_point_objective_secs** | **int** | Specifies the recovery point objective time user expects for this standby resource. | [optional] 
**datastore_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the datastore objects where this standby resource should be created. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**parent_object_id** | **int** | Specifies the object id for parent vCenter source where this standby resource should be created. | [optional] 
**rename_restored_object_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**resource_pool_object_id** | **int** | Specifies the object id for resource pool where this standby resource should be created. | [optional] 
**target_datastore_folder_object_id** | **int** | Specifies the object id for target datastore folder where disks for this standby resource should be placed. | [optional] 
**target_folder_object_id** | **int** | Specifies the object id for target vm folder where this standby resource should be created. | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_protection_group_standby_resource_params import VmwareProtectionGroupStandbyResourceParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareProtectionGroupStandbyResourceParams from a JSON string
vmware_protection_group_standby_resource_params_instance = VmwareProtectionGroupStandbyResourceParams.from_json(json)
# print the JSON string representation of the object
print(VmwareProtectionGroupStandbyResourceParams.to_json())

# convert the object into a dict
vmware_protection_group_standby_resource_params_dict = vmware_protection_group_standby_resource_params_instance.to_dict()
# create an instance of VmwareProtectionGroupStandbyResourceParams from a dict
vmware_protection_group_standby_resource_params_from_dict = VmwareProtectionGroupStandbyResourceParams.from_dict(vmware_protection_group_standby_resource_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


