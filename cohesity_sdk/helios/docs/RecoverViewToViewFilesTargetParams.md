# RecoverViewToViewFilesTargetParams

Specifies the params of the View recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_view_config** | [**NewViewFilesTargetParams**](NewViewFilesTargetParams.md) | Specifies the new destination View configuration parameters where the files will be recovered. This is mandatory if recoverToNewView is set to true. | [optional] 
**original_view_config** | [**OriginalViewFilesTargetParams**](OriginalViewFilesTargetParams.md) | Specifies the View configuration if files are being recovered to original View. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_view** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original View target. | 
**view_id** | **int** | Specifies the ID of the view. | [optional] 
**view_name** | **str** | Specifies the name of the new view that&#39;s the target for recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_view_to_view_files_target_params import RecoverViewToViewFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverViewToViewFilesTargetParams from a JSON string
recover_view_to_view_files_target_params_instance = RecoverViewToViewFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverViewToViewFilesTargetParams.to_json())

# convert the object into a dict
recover_view_to_view_files_target_params_dict = recover_view_to_view_files_target_params_instance.to_dict()
# create an instance of RecoverViewToViewFilesTargetParams from a dict
recover_view_to_view_files_target_params_from_dict = RecoverViewToViewFilesTargetParams.from_dict(recover_view_to_view_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


