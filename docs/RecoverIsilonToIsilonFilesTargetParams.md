# RecoverIsilonToIsilonFilesTargetParams

Specifies the params of the Isilon recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToIsilonFilesTargetParams**](RecoverOtherNasToIsilonFilesTargetParams.md) |  | [optional] 
**original_source_config** | [**OriginalIsilonFilesTargetParams**](OriginalIsilonFilesTargetParams.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Isilon target. | 

## Example

```python
from cohesity_sdk.models.recover_isilon_to_isilon_files_target_params import RecoverIsilonToIsilonFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverIsilonToIsilonFilesTargetParams from a JSON string
recover_isilon_to_isilon_files_target_params_instance = RecoverIsilonToIsilonFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverIsilonToIsilonFilesTargetParams.to_json())

# convert the object into a dict
recover_isilon_to_isilon_files_target_params_dict = recover_isilon_to_isilon_files_target_params_instance.to_dict()
# create an instance of RecoverIsilonToIsilonFilesTargetParams from a dict
recover_isilon_to_isilon_files_target_params_from_dict = RecoverIsilonToIsilonFilesTargetParams.from_dict(recover_isilon_to_isilon_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


