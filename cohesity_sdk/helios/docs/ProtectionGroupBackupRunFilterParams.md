# ProtectionGroupBackupRunFilterParams

Specifies the additional filtering params for backup runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_sla_violated** | **bool** | Specifies whether to only return activities which violated SLA. Default is false. | [optional] 
**protection_environment_types** | **List[str]** | Specifies the protection environment types to filter backup runs. | [optional] 
**run_types** | **List[str]** | Specifies the run types to filter backup runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_group_backup_run_filter_params import ProtectionGroupBackupRunFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupBackupRunFilterParams from a JSON string
protection_group_backup_run_filter_params_instance = ProtectionGroupBackupRunFilterParams.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupBackupRunFilterParams.to_json())

# convert the object into a dict
protection_group_backup_run_filter_params_dict = protection_group_backup_run_filter_params_instance.to_dict()
# create an instance of ProtectionGroupBackupRunFilterParams from a dict
protection_group_backup_run_filter_params_from_dict = ProtectionGroupBackupRunFilterParams.from_dict(protection_group_backup_run_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


