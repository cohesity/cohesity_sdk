# IncrementalBackupPolicy

Specifies incremental backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**IncrementalSchedule**](IncrementalSchedule.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.incremental_backup_policy import IncrementalBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of IncrementalBackupPolicy from a JSON string
incremental_backup_policy_instance = IncrementalBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(IncrementalBackupPolicy.to_json())

# convert the object into a dict
incremental_backup_policy_dict = incremental_backup_policy_instance.to_dict()
# create an instance of IncrementalBackupPolicy from a dict
incremental_backup_policy_from_dict = IncrementalBackupPolicy.from_dict(incremental_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


