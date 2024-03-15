# AntivirusScanConfig

Specifies the antivirus scan config settings for this View.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_timeout_usecs** | **int, none_type** | Specifies the maximum amount of time that a scan can take before timing out. | 
**block_access_on_scan_failure** | **bool, none_type** | Specifies whether block access to the file when antivirus scan fails. | [optional] 
**is_enabled** | **bool, none_type** | Specifies whether the antivirus service is enabled or not. | [optional] 
**maximum_scan_file_size** | **int, none_type** | Specifies maximum file size that will be sent to antivirus server for scanning. if greater than zero, the file size that exceeds this size would be skipped from virus scan. | [optional] 
**scan_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Files extension that meets these filter criteria will be sent to antivirus server for the scan. | [optional] 
**scan_on_access** | **bool, none_type** | Specifies whether to scan a file when it is opened. | [optional] 
**scan_on_close** | **bool, none_type** | Specifies whether to scan a file when it is closed after modify. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


