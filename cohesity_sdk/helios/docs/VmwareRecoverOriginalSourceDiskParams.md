# VmwareRecoverOriginalSourceDiskParams

Specifies disk specific parameters for performing a disk recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_id** | **int** | Specifies the ID of the datastore on which the specified disk will be spun up. | [optional] 
**disk_uuid** | **str** | Specifies the UUID of the source disk being recovered. | 
**overwrite_original_disk** | **bool** | Specifies whether or not to overwrite the original disk. If this is set to true, then datastoreId should not be specified. Otherwise, datastoreId must be specified. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_recover_original_source_disk_params import VmwareRecoverOriginalSourceDiskParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareRecoverOriginalSourceDiskParams from a JSON string
vmware_recover_original_source_disk_params_instance = VmwareRecoverOriginalSourceDiskParams.from_json(json)
# print the JSON string representation of the object
print(VmwareRecoverOriginalSourceDiskParams.to_json())

# convert the object into a dict
vmware_recover_original_source_disk_params_dict = vmware_recover_original_source_disk_params_instance.to_dict()
# create an instance of VmwareRecoverOriginalSourceDiskParams from a dict
vmware_recover_original_source_disk_params_from_dict = VmwareRecoverOriginalSourceDiskParams.from_dict(vmware_recover_original_source_disk_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


