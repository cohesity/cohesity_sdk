# SnapMirrorConfig

Specifies the snapshot backup configuration if S3 views are used for backing up NetApp Data-Protect volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incremental_prefix** | **str** | Specifies the incremental snapshot prefix value. | [optional] 
**view_id** | **int** | Specifies the Id of the S3 view where data need to be written. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snap_mirror_config import SnapMirrorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SnapMirrorConfig from a JSON string
snap_mirror_config_instance = SnapMirrorConfig.from_json(json)
# print the JSON string representation of the object
print(SnapMirrorConfig.to_json())

# convert the object into a dict
snap_mirror_config_dict = snap_mirror_config_instance.to_dict()
# create an instance of SnapMirrorConfig from a dict
snap_mirror_config_from_dict = SnapMirrorConfig.from_dict(snap_mirror_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


