# ObjectSnapshotVolumeInfo

Detail info of an object snapshot volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumes** | [**List[VolumeInfo]**](VolumeInfo.md) | Specifies a list of volume info. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_snapshot_volume_info import ObjectSnapshotVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSnapshotVolumeInfo from a JSON string
object_snapshot_volume_info_instance = ObjectSnapshotVolumeInfo.from_json(json)
# print the JSON string representation of the object
print(ObjectSnapshotVolumeInfo.to_json())

# convert the object into a dict
object_snapshot_volume_info_dict = object_snapshot_volume_info_instance.to_dict()
# create an instance of ObjectSnapshotVolumeInfo from a dict
object_snapshot_volume_info_from_dict = ObjectSnapshotVolumeInfo.from_dict(object_snapshot_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


