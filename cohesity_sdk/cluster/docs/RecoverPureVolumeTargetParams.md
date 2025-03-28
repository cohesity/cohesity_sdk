# RecoverPureVolumeTargetParams

Specifies the target object parameters to recover the Pure San Volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverPureSanVolumeNewSourceConfig**](RecoverPureSanVolumeNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverPureSanVolumeOriginalSourceConfig**](RecoverPureSanVolumeOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies whether to recover to a new source. | 
**use_thin_clone** | **bool** | Specifies whether to use thin clone to restore storage array snapshots. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_pure_volume_target_params import RecoverPureVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureVolumeTargetParams from a JSON string
recover_pure_volume_target_params_instance = RecoverPureVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPureVolumeTargetParams.to_json())

# convert the object into a dict
recover_pure_volume_target_params_dict = recover_pure_volume_target_params_instance.to_dict()
# create an instance of RecoverPureVolumeTargetParams from a dict
recover_pure_volume_target_params_from_dict = RecoverPureVolumeTargetParams.from_dict(recover_pure_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


