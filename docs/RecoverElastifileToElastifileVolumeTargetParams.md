# RecoverElastifileToElastifileVolumeTargetParams

Specifies the params of the Elastifile recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToElastifileVolumeTargetParams**](RecoverOtherNasToElastifileVolumeTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalElastifileTargetParams**](OriginalElastifileTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Elastifile target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_elastifile_to_elastifile_volume_target_params import RecoverElastifileToElastifileVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverElastifileToElastifileVolumeTargetParams from a JSON string
recover_elastifile_to_elastifile_volume_target_params_instance = RecoverElastifileToElastifileVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverElastifileToElastifileVolumeTargetParams.to_json())

# convert the object into a dict
recover_elastifile_to_elastifile_volume_target_params_dict = recover_elastifile_to_elastifile_volume_target_params_instance.to_dict()
# create an instance of RecoverElastifileToElastifileVolumeTargetParams from a dict
recover_elastifile_to_elastifile_volume_target_params_from_dict = RecoverElastifileToElastifileVolumeTargetParams.from_dict(recover_elastifile_to_elastifile_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


