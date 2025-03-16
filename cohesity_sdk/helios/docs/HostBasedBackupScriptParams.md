# HostBasedBackupScriptParams

Specifies params of a pre/post scripts to be executed before and after a backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ScriptHost**](ScriptHost.md) |  | 
**post_backup_script** | [**CommonPostBackupScriptParams**](CommonPostBackupScriptParams.md) |  | [optional] 
**post_script** | [**CommonPostBackupScriptParams**](CommonPostBackupScriptParams.md) |  | [optional] 
**post_snapshot_script** | [**CommonPostBackupScriptParams**](CommonPostBackupScriptParams.md) |  | [optional] 
**pre_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.host_based_backup_script_params import HostBasedBackupScriptParams

# TODO update the JSON string below
json = "{}"
# create an instance of HostBasedBackupScriptParams from a JSON string
host_based_backup_script_params_instance = HostBasedBackupScriptParams.from_json(json)
# print the JSON string representation of the object
print(HostBasedBackupScriptParams.to_json())

# convert the object into a dict
host_based_backup_script_params_dict = host_based_backup_script_params_instance.to_dict()
# create an instance of HostBasedBackupScriptParams from a dict
host_based_backup_script_params_from_dict = HostBasedBackupScriptParams.from_dict(host_based_backup_script_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


