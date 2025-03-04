# VcenterRegistrationParams

Specifies parameters to register VMware vCenter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**ca_cert** | **str** | Specifies the CA certificate to enable SSL communication between host and cluster. | [optional] 
**data_store_params** | [**List[DatastoreParams]**](DatastoreParams.md) | Specifies datastore specific parameters. | [optional] 
**link_vms_across_vcenter** | **bool** | Specifies if the VM linking feature is enabled for the VCenter. If enabled, migrated VMs present in the VCenter which earlier belonged to some other VCenter will be linked during EH refresh. | [optional] 
**min_free_datastore_space_for_backup_gb** | **int** | Specifies the minimum free space (in GB) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**min_free_datastore_space_for_backup_percentage** | **int** | Specifies the minimum free space (in percentage) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**throttling_params** | [**VmwareThrottlingParams**](VmwareThrottlingParams.md) |  | [optional] 
**use_vm_bios_uuid** | **bool** | Specifies to use VM BIOS UUID to track virtual machines in the host. | [optional] 

## Example

```python
from cohesity_sdk.models.vcenter_registration_params import VcenterRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of VcenterRegistrationParams from a JSON string
vcenter_registration_params_instance = VcenterRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(VcenterRegistrationParams.to_json())

# convert the object into a dict
vcenter_registration_params_dict = vcenter_registration_params_instance.to_dict()
# create an instance of VcenterRegistrationParams from a dict
vcenter_registration_params_from_dict = VcenterRegistrationParams.from_dict(vcenter_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


