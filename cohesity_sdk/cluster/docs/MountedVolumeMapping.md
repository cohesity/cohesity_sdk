# MountedVolumeMapping

Specifies the mapping of original volume and mounted volume after Instant Volume Mount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_type** | **str** | Specifies the type of the file system of the volume. | [optional] 
**mounted_volume** | **str** | Specifies the name of the point where the volume is mounted. | [optional] 
**original_volume** | **str** | Specifies the name of the original volume. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mounted_volume_mapping import MountedVolumeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of MountedVolumeMapping from a JSON string
mounted_volume_mapping_instance = MountedVolumeMapping.from_json(json)
# print the JSON string representation of the object
print(MountedVolumeMapping.to_json())

# convert the object into a dict
mounted_volume_mapping_dict = mounted_volume_mapping_instance.to_dict()
# create an instance of MountedVolumeMapping from a dict
mounted_volume_mapping_from_dict = MountedVolumeMapping.from_dict(mounted_volume_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


