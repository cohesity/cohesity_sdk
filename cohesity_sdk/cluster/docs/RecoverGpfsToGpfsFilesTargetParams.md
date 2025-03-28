# RecoverGpfsToGpfsFilesTargetParams

Specifies the params of the GPFS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToGpfsFilesTargetParams**](RecoverOtherNasToGpfsFilesTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalGpfsFilesTargetParams**](OriginalGpfsFilesTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original GPFS target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gpfs_to_gpfs_files_target_params import RecoverGpfsToGpfsFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGpfsToGpfsFilesTargetParams from a JSON string
recover_gpfs_to_gpfs_files_target_params_instance = RecoverGpfsToGpfsFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGpfsToGpfsFilesTargetParams.to_json())

# convert the object into a dict
recover_gpfs_to_gpfs_files_target_params_dict = recover_gpfs_to_gpfs_files_target_params_instance.to_dict()
# create an instance of RecoverGpfsToGpfsFilesTargetParams from a dict
recover_gpfs_to_gpfs_files_target_params_from_dict = RecoverGpfsToGpfsFilesTargetParams.from_dict(recover_gpfs_to_gpfs_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


