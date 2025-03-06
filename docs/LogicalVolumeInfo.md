# LogicalVolumeInfo

Specifies the logical volume info for LVM or LDM volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_tree** | [**DeviceTreeNode**](DeviceTreeNode.md) |  | [optional] 
**logical_volume_name** | **str** | Specifies the logical volume name. | [optional] 
**logical_volume_uuid** | **str** | Specifies the logical volume uuid. | [optional] 
**volume_group_name** | **str** | Specifies the volume group name. | [optional] 
**volume_group_uuid** | **str** | Specifies the volume group uuid. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.logical_volume_info import LogicalVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalVolumeInfo from a JSON string
logical_volume_info_instance = LogicalVolumeInfo.from_json(json)
# print the JSON string representation of the object
print(LogicalVolumeInfo.to_json())

# convert the object into a dict
logical_volume_info_dict = logical_volume_info_instance.to_dict()
# create an instance of LogicalVolumeInfo from a dict
logical_volume_info_from_dict = LogicalVolumeInfo.from_dict(logical_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


