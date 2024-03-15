# Office365UserOneDriveObjectProtectionParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_folders** | **[str], none_type** | Specifies filters to match OneDrive folders which should be excluded when backing up office365 onedrive source. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all the OneDrive will be protected. | [optional] 
**preservation_hold_library_params** | [**Office365PreservationHoldLibraryParams**](Office365PreservationHoldLibraryParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


