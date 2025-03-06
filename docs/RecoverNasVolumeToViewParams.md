# RecoverNasVolumeToViewParams

Specifies the recovery target configuration if NAS volumes are being recovered as a Cohesity view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos_policy** | [**NasQosPolicy**](NasQosPolicy.md) |  | [optional] 
**view_name** | **str** | Specifies the name of the view. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_nas_volume_to_view_params import RecoverNasVolumeToViewParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNasVolumeToViewParams from a JSON string
recover_nas_volume_to_view_params_instance = RecoverNasVolumeToViewParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNasVolumeToViewParams.to_json())

# convert the object into a dict
recover_nas_volume_to_view_params_dict = recover_nas_volume_to_view_params_instance.to_dict()
# create an instance of RecoverNasVolumeToViewParams from a dict
recover_nas_volume_to_view_params_from_dict = RecoverNasVolumeToViewParams.from_dict(recover_nas_volume_to_view_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


