# Office365SharePointProtectionGroupParams

Specifies the parameters which are specific to Office 365 SharePoint related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_paths** | **List[str]** | Array of paths to be excluded from backup. Specifies list of doclib/directory paths which should be excluded when backing up Office 365 source. supported exclusion: - doclib exclusion: whole doclib is excluded from backup. sample: /Doclib1 - directory exclusion: specified path in doclib will be excluded from backup. sample: /Doclib1/folderA/forderB Doclibs can be specified by either a) Doclib name - eg, Documents. b) Drive id of doclib - b!ZMSl2JRm0UeXLHfHR1m-iuD10p0CIV9qSa6TtgM Regular expressions are not supported. If not specified, all the doclibs within sharepoint site will be protected. | [optional] 
**preservation_hold_library_params** | [**Office365PreservationHoldLibraryParams**](Office365PreservationHoldLibraryParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.office365_share_point_protection_group_params import Office365SharePointProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365SharePointProtectionGroupParams from a JSON string
office365_share_point_protection_group_params_instance = Office365SharePointProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(Office365SharePointProtectionGroupParams.to_json())

# convert the object into a dict
office365_share_point_protection_group_params_dict = office365_share_point_protection_group_params_instance.to_dict()
# create an instance of Office365SharePointProtectionGroupParams from a dict
office365_share_point_protection_group_params_from_dict = Office365SharePointProtectionGroupParams.from_dict(office365_share_point_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


