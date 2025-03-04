# CloseSmbFileOpenParams

Specifies params to close active SMB file open.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** | Specifies the filepath in the Cohesity View relative to the root filesystem. If this field is specified, viewName field must also be specified. | 
**open_id** | **int** | Specifies the id of the active open. | 
**view_name** | **str** | Specifies the name of the Cohesity View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. | 

## Example

```python
from cohesity_sdk.models.close_smb_file_open_params import CloseSmbFileOpenParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloseSmbFileOpenParams from a JSON string
close_smb_file_open_params_instance = CloseSmbFileOpenParams.from_json(json)
# print the JSON string representation of the object
print(CloseSmbFileOpenParams.to_json())

# convert the object into a dict
close_smb_file_open_params_dict = close_smb_file_open_params_instance.to_dict()
# create an instance of CloseSmbFileOpenParams from a dict
close_smb_file_open_params_from_dict = CloseSmbFileOpenParams.from_dict(close_smb_file_open_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


