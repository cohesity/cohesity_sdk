# BackupRunFilterParams

Specifies the additional filtering params for backup runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_environment_types** | **List[str]** | Specifies the protection environment types to filter backup runs. | [optional] 
**run_types** | **List[str]** | Specifies the run types to filter backup runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.backup_run_filter_params import BackupRunFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRunFilterParams from a JSON string
backup_run_filter_params_instance = BackupRunFilterParams.from_json(json)
# print the JSON string representation of the object
print(BackupRunFilterParams.to_json())

# convert the object into a dict
backup_run_filter_params_dict = backup_run_filter_params_instance.to_dict()
# create an instance of BackupRunFilterParams from a dict
backup_run_filter_params_from_dict = BackupRunFilterParams.from_dict(backup_run_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


