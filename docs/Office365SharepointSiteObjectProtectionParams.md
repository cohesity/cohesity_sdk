# Office365SharepointSiteObjectProtectionParams

Specifies the params to create a Sharepoint site Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[Office365ObjectProtectionObjectParams]**](Office365ObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**exclude_paths** | **[str], none_type** | Array of paths to be excluded from backup. Specifies list of doclib/directory paths which should be excluded when backing up Office 365 source. supported exclusion: - doclib exclusion: whole doclib is excluded from backup. sample: /Doclib1 - directory exclusion: specified path in doclib will be excluded from backup. sample: /Doclib1/folderA/forderB Doclibs can be specified by either a) Doclib name - eg, Documents. b) Drive id of doclib - b!ZMSl2JRm0UeXLHfHR1m-iuD10p0CIV9qSa6TtgM Regular expressions are not supported. If not specified, all the doclibs within sharepoint site will be protected. | [optional] 
**preservation_hold_library_params** | [**Office365PreservationHoldLibraryParams**](Office365PreservationHoldLibraryParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


