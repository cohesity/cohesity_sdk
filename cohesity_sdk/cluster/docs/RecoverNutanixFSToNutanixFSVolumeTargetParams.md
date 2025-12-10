# RecoverNutanixFSToNutanixFSVolumeTargetParams

Specifies the params of the NutanixFS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToNutanixFSVolumeTargetParams**](RecoverOtherNasToNutanixFSVolumeTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalNutanixFSTargetParams**](OriginalNutanixFSTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original NutanixFS target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_nutanix_fsto_nutanix_fs_volume_target_params import RecoverNutanixFSToNutanixFSVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNutanixFSToNutanixFSVolumeTargetParams from a JSON string
recover_nutanix_fsto_nutanix_fs_volume_target_params_instance = RecoverNutanixFSToNutanixFSVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNutanixFSToNutanixFSVolumeTargetParams.to_json())

# convert the object into a dict
recover_nutanix_fsto_nutanix_fs_volume_target_params_dict = recover_nutanix_fsto_nutanix_fs_volume_target_params_instance.to_dict()
# create an instance of RecoverNutanixFSToNutanixFSVolumeTargetParams from a dict
recover_nutanix_fsto_nutanix_fs_volume_target_params_from_dict = RecoverNutanixFSToNutanixFSVolumeTargetParams.from_dict(recover_nutanix_fsto_nutanix_fs_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


