# CommonObjectSnapshotVolumeParams

Specifies volume info of snapshot across all enviroments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumes** | [**List[VolumeInfo]**](VolumeInfo.md) | Specifies a list of volume info. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_object_snapshot_volume_params import CommonObjectSnapshotVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonObjectSnapshotVolumeParams from a JSON string
common_object_snapshot_volume_params_instance = CommonObjectSnapshotVolumeParams.from_json(json)
# print the JSON string representation of the object
print(CommonObjectSnapshotVolumeParams.to_json())

# convert the object into a dict
common_object_snapshot_volume_params_dict = common_object_snapshot_volume_params_instance.to_dict()
# create an instance of CommonObjectSnapshotVolumeParams from a dict
common_object_snapshot_volume_params_from_dict = CommonObjectSnapshotVolumeParams.from_dict(common_object_snapshot_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


