# LogBackupPolicy

Specifies log backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**Retention**](Retention.md) |  | 
**schedule** | [**LogSchedule**](LogSchedule.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.log_backup_policy import LogBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of LogBackupPolicy from a JSON string
log_backup_policy_instance = LogBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(LogBackupPolicy.to_json())

# convert the object into a dict
log_backup_policy_dict = log_backup_policy_instance.to_dict()
# create an instance of LogBackupPolicy from a dict
log_backup_policy_from_dict = LogBackupPolicy.from_dict(log_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


