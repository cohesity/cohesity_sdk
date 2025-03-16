# RecoverIsilonToIsilonVolumeTargetParams

Specifies the params of the Isilon recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToIsilonVolumeTargetParams**](RecoverOtherNasToIsilonVolumeTargetParams.md) | Specifies the new destination Source configuration parameters where the volumes will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | [**OriginalIsilonTargetParams**](OriginalIsilonTargetParams.md) | Specifies the Source configuration if volumes are being recovered to original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Isilon target. | 

## Example

```python
from cohesity_sdk.helios.models.recover_isilon_to_isilon_volume_target_params import RecoverIsilonToIsilonVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverIsilonToIsilonVolumeTargetParams from a JSON string
recover_isilon_to_isilon_volume_target_params_instance = RecoverIsilonToIsilonVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverIsilonToIsilonVolumeTargetParams.to_json())

# convert the object into a dict
recover_isilon_to_isilon_volume_target_params_dict = recover_isilon_to_isilon_volume_target_params_instance.to_dict()
# create an instance of RecoverIsilonToIsilonVolumeTargetParams from a dict
recover_isilon_to_isilon_volume_target_params_from_dict = RecoverIsilonToIsilonVolumeTargetParams.from_dict(recover_isilon_to_isilon_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


