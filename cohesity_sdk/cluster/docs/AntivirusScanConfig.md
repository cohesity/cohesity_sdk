# AntivirusScanConfig

Specifies the antivirus scan config settings for this View.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_timeout_usecs** | **int, none_type** | Specifies the maximum amount of time that a scan can take before timing out. | 
**block_access_on_scan_failure** | **bool, none_type** | Specifies whether block access to the file when antivirus scan fails. | [optional] 
**is_enabled** | **bool, none_type** | Specifies whether the antivirus service is enabled or not. | [optional] 
**maximum_scan_file_size** | **int, none_type** | Specifies maximum file size that will be sent to antivirus server for scanning. if greater than zero, the file size that exceeds this size would be skipped from virus scan. | [optional] 
**prefix_scan_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | For S3 usage only. Prefixes that meets these filter criteria will be sent to antivirus server for the scan. This filter is case-sensitive. | [optional] 
**s3_tagging_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | For S3 usage only. If set, only objects with these taggings will be scanned or not scanned, depending on the mode. | [optional] 
**scan_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Files extension that meets these filter criteria will be sent to antivirus server for the scan. This filter is case-insensitive. | [optional] 
**scan_on_access** | **bool, none_type** | Specifies whether to scan a SMB file or S3 object before it is opened/GET. | [optional] 
**scan_on_close** | **bool, none_type** | Specifies whether to scan a SMB file when it is closed after modify. | [optional] 
**scan_on_put** | **bool, none_type** | Specifies whether to scan a S3 object after it is PUT. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


