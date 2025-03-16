# VolumeInfo

Specifies info of logical volume (filesystem).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filesystem_type** | **str** | Specifies the filesystem type. | [optional] 
**filesystem_uuid** | **str** | Specifies the filesystem uuid. | [optional] 
**is_dedupe** | **bool** | Specifies if this is NTFS dedupe volume | [optional] 
**is_supported** | **bool** | Specifies if this volume is supported. | [optional] 
**logical_volume_info** | [**LogicalVolumeInfo**](LogicalVolumeInfo.md) | Specifies the logical volume info. This fields is for &#39;LVM&#39; and &#39;LDM&#39; volume type only. | [optional] 
**name** | **str** | Specifies the volume name. | [optional] 
**volume_guid** | **str** | Specifies the volume guid. | [optional] 
**volume_size_in_bytes** | **int** | Specifies volume size in bytes. | [optional] 
**volume_type** | **str** | Specifies the volume type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.volume_info import VolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeInfo from a JSON string
volume_info_instance = VolumeInfo.from_json(json)
# print the JSON string representation of the object
print(VolumeInfo.to_json())

# convert the object into a dict
volume_info_dict = volume_info_instance.to_dict()
# create an instance of VolumeInfo from a dict
volume_info_from_dict = VolumeInfo.from_dict(volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


