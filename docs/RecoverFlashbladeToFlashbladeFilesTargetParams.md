# RecoverFlashbladeToFlashbladeFilesTargetParams

Specifies the params of the Flashblade recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToFlashbladeFilesTargetParams**](RecoverOtherNasToFlashbladeFilesTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalFlashbladeFilesTargetParams**](OriginalFlashbladeFilesTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Flashblade target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_flashblade_to_flashblade_files_target_params import RecoverFlashbladeToFlashbladeFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverFlashbladeToFlashbladeFilesTargetParams from a JSON string
recover_flashblade_to_flashblade_files_target_params_instance = RecoverFlashbladeToFlashbladeFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverFlashbladeToFlashbladeFilesTargetParams.to_json())

# convert the object into a dict
recover_flashblade_to_flashblade_files_target_params_dict = recover_flashblade_to_flashblade_files_target_params_instance.to_dict()
# create an instance of RecoverFlashbladeToFlashbladeFilesTargetParams from a dict
recover_flashblade_to_flashblade_files_target_params_from_dict = RecoverFlashbladeToFlashbladeFilesTargetParams.from_dict(recover_flashblade_to_flashblade_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


