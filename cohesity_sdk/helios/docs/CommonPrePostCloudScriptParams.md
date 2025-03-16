# CommonPrePostCloudScriptParams

Specifies the common params for PrePost backup scripts specific for cloud-adapters. They have two different scripts for the two different shell types - windows and linux

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linux_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**windows_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_pre_post_cloud_script_params import CommonPrePostCloudScriptParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPrePostCloudScriptParams from a JSON string
common_pre_post_cloud_script_params_instance = CommonPrePostCloudScriptParams.from_json(json)
# print the JSON string representation of the object
print(CommonPrePostCloudScriptParams.to_json())

# convert the object into a dict
common_pre_post_cloud_script_params_dict = common_pre_post_cloud_script_params_instance.to_dict()
# create an instance of CommonPrePostCloudScriptParams from a dict
common_pre_post_cloud_script_params_from_dict = CommonPrePostCloudScriptParams.from_dict(common_pre_post_cloud_script_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


