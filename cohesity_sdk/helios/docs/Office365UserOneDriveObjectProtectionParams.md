# Office365UserOneDriveObjectProtectionParams

Specifies the params to create a User OneDrive Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[Office365ObjectProtectionObjectParams]**](Office365ObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**exclude_folders** | **List[str]** | Specifies filters to match OneDrive folders which should be excluded when backing up office365 onedrive source. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all the OneDrive will be protected. | [optional] 
**preservation_hold_library_params** | [**Office365PreservationHoldLibraryParams**](Office365PreservationHoldLibraryParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.office365_user_one_drive_object_protection_params import Office365UserOneDriveObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365UserOneDriveObjectProtectionParams from a JSON string
office365_user_one_drive_object_protection_params_instance = Office365UserOneDriveObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(Office365UserOneDriveObjectProtectionParams.to_json())

# convert the object into a dict
office365_user_one_drive_object_protection_params_dict = office365_user_one_drive_object_protection_params_instance.to_dict()
# create an instance of Office365UserOneDriveObjectProtectionParams from a dict
office365_user_one_drive_object_protection_params_from_dict = Office365UserOneDriveObjectProtectionParams.from_dict(office365_user_one_drive_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


