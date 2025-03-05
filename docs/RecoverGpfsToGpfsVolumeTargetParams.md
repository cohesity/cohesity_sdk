# RecoverGpfsToGpfsVolumeTargetParams

Specifies the params of the GPFS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalGpfsTargetParams**](OriginalGpfsTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original GPFS target. | 

## Example

```python
from cohesity_sdk.models.recover_gpfs_to_gpfs_volume_target_params import RecoverGpfsToGpfsVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGpfsToGpfsVolumeTargetParams from a JSON string
recover_gpfs_to_gpfs_volume_target_params_instance = RecoverGpfsToGpfsVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGpfsToGpfsVolumeTargetParams.to_json())

# convert the object into a dict
recover_gpfs_to_gpfs_volume_target_params_dict = recover_gpfs_to_gpfs_volume_target_params_instance.to_dict()
# create an instance of RecoverGpfsToGpfsVolumeTargetParams from a dict
recover_gpfs_to_gpfs_volume_target_params_from_dict = RecoverGpfsToGpfsVolumeTargetParams.from_dict(recover_gpfs_to_gpfs_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


