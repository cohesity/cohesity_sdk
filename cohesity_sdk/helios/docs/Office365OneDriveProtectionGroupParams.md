# Office365OneDriveProtectionGroupParams

Specifies the parameters which are specific to Office 365 OneDrive related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_folders** | **[str], none_type** | Array of Excluded OneDrive folders. Specifies filters to match OneDrive folders which should be excluded when backing up Office 365 source. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all the mailboxes will be protected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


