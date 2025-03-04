# CommonPreBackupScriptParams

Specifies the common params for PreBackup scripts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Specifies whether the script should be enabled, default value set to true. | [optional] 
**params** | **str** | Specifies the arguments or parameters and values to pass into the remote script. For example if the script expects values for the &#39;database&#39; and &#39;user&#39; parameters, specify the parameters and values using the following string: \&quot;database&#x3D;myDatabase user&#x3D;me\&quot;. | [optional] 
**path** | **str** | Specifies the absolute path to the script on the remote host. | 
**timeout_secs** | **int** | Specifies the timeout of the script in seconds. The script will be killed if it exceeds this value. By default, no timeout will occur if left empty. | [optional] 
**continue_on_error** | **bool** | Specifies if the script needs to continue even if there is an occurence of an error. If this flag is set to true, then Backup Run will start even if the pre backup script fails. If not specified or false, then backup run will not start when script fails. | [optional] 

## Example

```python
from cohesity_sdk.models.common_pre_backup_script_params import CommonPreBackupScriptParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPreBackupScriptParams from a JSON string
common_pre_backup_script_params_instance = CommonPreBackupScriptParams.from_json(json)
# print the JSON string representation of the object
print(CommonPreBackupScriptParams.to_json())

# convert the object into a dict
common_pre_backup_script_params_dict = common_pre_backup_script_params_instance.to_dict()
# create an instance of CommonPreBackupScriptParams from a dict
common_pre_backup_script_params_from_dict = CommonPreBackupScriptParams.from_dict(common_pre_backup_script_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


