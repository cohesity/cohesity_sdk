# AntivirusScanConfig

Specifies the antivirus scan config settings for this View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_access_on_scan_failure** | **bool** | Specifies whether block access to the file when antivirus scan fails. | [optional] 
**is_enabled** | **bool** | Specifies whether the antivirus service is enabled or not. | [optional] 
**maximum_scan_file_size** | **int** | Specifies maximum file size that will be sent to antivirus server for scanning. if greater than zero, the file size that exceeds this size would be skipped from virus scan. | [optional] 
**scan_filter** | [**FileExtensionFilter**](FileExtensionFilter.md) |  | [optional] 
**scan_on_access** | **bool** | Specifies whether to scan a file when it is opened. | [optional] 
**scan_on_close** | **bool** | Specifies whether to scan a file when it is closed after modify. | [optional] 
**scan_timeout_usecs** | **int** | Specifies the maximum amount of time that a scan can take before timing out. | 

## Example

```python
from cohesity_sdk.models.antivirus_scan_config import AntivirusScanConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AntivirusScanConfig from a JSON string
antivirus_scan_config_instance = AntivirusScanConfig.from_json(json)
# print the JSON string representation of the object
print(AntivirusScanConfig.to_json())

# convert the object into a dict
antivirus_scan_config_dict = antivirus_scan_config_instance.to_dict()
# create an instance of AntivirusScanConfig from a dict
antivirus_scan_config_from_dict = AntivirusScanConfig.from_dict(antivirus_scan_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


