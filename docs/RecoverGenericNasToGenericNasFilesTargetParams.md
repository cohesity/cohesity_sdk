# RecoverGenericNasToGenericNasFilesTargetParams

Specifies the params of the Generic Nas recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToGenericNasFilesTargetParams**](RecoverOtherNasToGenericNasFilesTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalGenericNasFilesTargetParams**](OriginalGenericNasFilesTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Generic Nas target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_generic_nas_to_generic_nas_files_target_params import RecoverGenericNasToGenericNasFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGenericNasToGenericNasFilesTargetParams from a JSON string
recover_generic_nas_to_generic_nas_files_target_params_instance = RecoverGenericNasToGenericNasFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGenericNasToGenericNasFilesTargetParams.to_json())

# convert the object into a dict
recover_generic_nas_to_generic_nas_files_target_params_dict = recover_generic_nas_to_generic_nas_files_target_params_instance.to_dict()
# create an instance of RecoverGenericNasToGenericNasFilesTargetParams from a dict
recover_generic_nas_to_generic_nas_files_target_params_from_dict = RecoverGenericNasToGenericNasFilesTargetParams.from_dict(recover_generic_nas_to_generic_nas_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


