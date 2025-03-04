# CloudBackupScriptParams

Specifies params of a pre/post scripts to be executed before and after a backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_backup_script** | [**CommonPrePostCloudScriptParams**](CommonPrePostCloudScriptParams.md) |  | [optional] 
**post_snapshot_script** | [**CommonPrePostCloudScriptParams**](CommonPrePostCloudScriptParams.md) |  | [optional] 
**pre_backup_script** | [**CommonPrePostCloudScriptParams**](CommonPrePostCloudScriptParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.cloud_backup_script_params import CloudBackupScriptParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloudBackupScriptParams from a JSON string
cloud_backup_script_params_instance = CloudBackupScriptParams.from_json(json)
# print the JSON string representation of the object
print(CloudBackupScriptParams.to_json())

# convert the object into a dict
cloud_backup_script_params_dict = cloud_backup_script_params_instance.to_dict()
# create an instance of CloudBackupScriptParams from a dict
cloud_backup_script_params_from_dict = CloudBackupScriptParams.from_dict(cloud_backup_script_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


