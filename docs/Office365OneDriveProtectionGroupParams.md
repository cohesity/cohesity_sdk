# Office365OneDriveProtectionGroupParams

Specifies the parameters which are specific to Office 365 OneDrive related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_folders** | **List[str]** | Array of Excluded OneDrive folders. Specifies filters to match OneDrive folders which should be excluded when backing up Office 365 source. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all the mailboxes will be protected. | [optional] 
**preservation_hold_library_params** | [**Office365PreservationHoldLibraryParams**](Office365PreservationHoldLibraryParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.office365_one_drive_protection_group_params import Office365OneDriveProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365OneDriveProtectionGroupParams from a JSON string
office365_one_drive_protection_group_params_instance = Office365OneDriveProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(Office365OneDriveProtectionGroupParams.to_json())

# convert the object into a dict
office365_one_drive_protection_group_params_dict = office365_one_drive_protection_group_params_instance.to_dict()
# create an instance of Office365OneDriveProtectionGroupParams from a dict
office365_one_drive_protection_group_params_from_dict = Office365OneDriveProtectionGroupParams.from_dict(office365_one_drive_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


