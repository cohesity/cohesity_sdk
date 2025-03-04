# RecoverNetappToNetappVolumeTargetParams

Specifies the params of the Netapp recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToNetappVolumeTargetParams**](RecoverOtherNasToNetappVolumeTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalNetappTargetParams**](OriginalNetappTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Netapp target. | 

## Example

```python
from cohesity_sdk.models.recover_netapp_to_netapp_volume_target_params import RecoverNetappToNetappVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNetappToNetappVolumeTargetParams from a JSON string
recover_netapp_to_netapp_volume_target_params_instance = RecoverNetappToNetappVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNetappToNetappVolumeTargetParams.to_json())

# convert the object into a dict
recover_netapp_to_netapp_volume_target_params_dict = recover_netapp_to_netapp_volume_target_params_instance.to_dict()
# create an instance of RecoverNetappToNetappVolumeTargetParams from a dict
recover_netapp_to_netapp_volume_target_params_from_dict = RecoverNetappToNetappVolumeTargetParams.from_dict(recover_netapp_to_netapp_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


