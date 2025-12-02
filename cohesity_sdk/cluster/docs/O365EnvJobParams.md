# O365EnvJobParams

Specifies job parameters applicable for all 'kVMware' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onedrive_backup_params** | [**OnedriveBackupParams**](OnedriveBackupParams.md) |  | [optional] 
**outlook_backup_params** | [**OutlookBackupParams**](OutlookBackupParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.o365_env_job_params import O365EnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of O365EnvJobParams from a JSON string
o365_env_job_params_instance = O365EnvJobParams.from_json(json)
# print the JSON string representation of the object
print(O365EnvJobParams.to_json())

# convert the object into a dict
o365_env_job_params_dict = o365_env_job_params_instance.to_dict()
# create an instance of O365EnvJobParams from a dict
o365_env_job_params_from_dict = O365EnvJobParams.from_dict(o365_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


