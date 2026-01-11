# Office365PublicFoldersProtectionGroupParams

Specifies the parameters which are specific to Office 365 PublicFolders related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_folders** | **[str], none_type** | Array of Excluded Public folders. Specifies filters to match PublicFolder folders which should be excluded when backing up Office 365 source. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all the PublicFolders will be protected. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


