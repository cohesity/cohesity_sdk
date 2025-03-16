# SmbActiveFilePath

Specifies a file path in an SMB view that has active sessions and opens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_sessions** | [**List[SmbActiveSession]**](SmbActiveSession.md) | Specifies an active session where the file is open. | [optional] 
**file_path** | **str** | Specifies the filepath in the view. | [optional] 
**view_id** | **int** | Specifies the id of the View. | [optional] 
**view_name** | **str** | Specifies the name of the View. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.smb_active_file_path import SmbActiveFilePath

# TODO update the JSON string below
json = "{}"
# create an instance of SmbActiveFilePath from a JSON string
smb_active_file_path_instance = SmbActiveFilePath.from_json(json)
# print the JSON string representation of the object
print(SmbActiveFilePath.to_json())

# convert the object into a dict
smb_active_file_path_dict = smb_active_file_path_instance.to_dict()
# create an instance of SmbActiveFilePath from a dict
smb_active_file_path_from_dict = SmbActiveFilePath.from_dict(smb_active_file_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


