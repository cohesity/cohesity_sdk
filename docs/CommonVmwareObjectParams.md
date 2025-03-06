# CommonVmwareObjectParams

Specifies the common object parameters required for VMware protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[DiskInfo]**](DiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**truncate_exchange_logs** | **bool** | Specifies whether or not to truncate MS Exchange logs while taking an app consistent snapshot of this object. This is only applicable to objects which have a registered MS Exchange app. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_vmware_object_params import CommonVmwareObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonVmwareObjectParams from a JSON string
common_vmware_object_params_instance = CommonVmwareObjectParams.from_json(json)
# print the JSON string representation of the object
print(CommonVmwareObjectParams.to_json())

# convert the object into a dict
common_vmware_object_params_dict = common_vmware_object_params_instance.to_dict()
# create an instance of CommonVmwareObjectParams from a dict
common_vmware_object_params_from_dict = CommonVmwareObjectParams.from_dict(common_vmware_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


