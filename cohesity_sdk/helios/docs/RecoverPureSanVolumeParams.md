# RecoverPureSanVolumeParams

Specifies the parameters to recover Pure SAN Volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pure_target_params** | [**RecoverPureVolumeTargetParams**](RecoverPureVolumeTargetParams.md) | Specifies the parameters of the Pure SAN volume to recover to. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding target params must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_pure_san_volume_params import RecoverPureSanVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureSanVolumeParams from a JSON string
recover_pure_san_volume_params_instance = RecoverPureSanVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPureSanVolumeParams.to_json())

# convert the object into a dict
recover_pure_san_volume_params_dict = recover_pure_san_volume_params_instance.to_dict()
# create an instance of RecoverPureSanVolumeParams from a dict
recover_pure_san_volume_params_from_dict = RecoverPureSanVolumeParams.from_dict(recover_pure_san_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


