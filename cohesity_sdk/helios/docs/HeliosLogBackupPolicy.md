# HeliosLogBackupPolicy

Specifies log backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 
**schedule** | [**HeliosLogSchedule**](HeliosLogSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_log_backup_policy import HeliosLogBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosLogBackupPolicy from a JSON string
helios_log_backup_policy_instance = HeliosLogBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosLogBackupPolicy.to_json())

# convert the object into a dict
helios_log_backup_policy_dict = helios_log_backup_policy_instance.to_dict()
# create an instance of HeliosLogBackupPolicy from a dict
helios_log_backup_policy_from_dict = HeliosLogBackupPolicy.from_dict(helios_log_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


