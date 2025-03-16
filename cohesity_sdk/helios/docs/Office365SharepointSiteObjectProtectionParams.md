# Office365SharepointSiteObjectProtectionParams

Specifies the params to create a Sharepoint site Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[Office365ObjectProtectionObjectParams]**](Office365ObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**exclude_paths** | **List[str]** | Array of paths to be excluded from backup. Specifies list of doclib/directory paths which should be excluded when backing up Office 365 source. supported exclusion: - doclib exclusion: whole doclib is excluded from backup. sample: /Doclib1 - directory exclusion: specified path in doclib will be excluded from backup. sample: /Doclib1/folderA/forderB Doclibs can be specified by either a) Doclib name - eg, Documents. b) Drive id of doclib - b!ZMSl2JRm0UeXLHfHR1m-iuD10p0CIV9qSa6TtgM Regular expressions are not supported. If not specified, all the doclibs within sharepoint site will be protected. | [optional] 
**preservation_hold_library_params** | [**Office365PreservationHoldLibraryParams**](Office365PreservationHoldLibraryParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.office365_sharepoint_site_object_protection_params import Office365SharepointSiteObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365SharepointSiteObjectProtectionParams from a JSON string
office365_sharepoint_site_object_protection_params_instance = Office365SharepointSiteObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(Office365SharepointSiteObjectProtectionParams.to_json())

# convert the object into a dict
office365_sharepoint_site_object_protection_params_dict = office365_sharepoint_site_object_protection_params_instance.to_dict()
# create an instance of Office365SharepointSiteObjectProtectionParams from a dict
office365_sharepoint_site_object_protection_params_from_dict = Office365SharepointSiteObjectProtectionParams.from_dict(office365_sharepoint_site_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


