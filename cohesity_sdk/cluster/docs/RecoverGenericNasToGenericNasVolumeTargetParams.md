# RecoverGenericNasToGenericNasVolumeTargetParams

Specifies the params of the Generic NAS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToGenericNasVolumeTargetParams**](RecoverOtherNasToGenericNasVolumeTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalGenericNasTargetParams**](OriginalGenericNasTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Generic NAS target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_generic_nas_to_generic_nas_volume_target_params import RecoverGenericNasToGenericNasVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGenericNasToGenericNasVolumeTargetParams from a JSON string
recover_generic_nas_to_generic_nas_volume_target_params_instance = RecoverGenericNasToGenericNasVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGenericNasToGenericNasVolumeTargetParams.to_json())

# convert the object into a dict
recover_generic_nas_to_generic_nas_volume_target_params_dict = recover_generic_nas_to_generic_nas_volume_target_params_instance.to_dict()
# create an instance of RecoverGenericNasToGenericNasVolumeTargetParams from a dict
recover_generic_nas_to_generic_nas_volume_target_params_from_dict = RecoverGenericNasToGenericNasVolumeTargetParams.from_dict(recover_generic_nas_to_generic_nas_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


