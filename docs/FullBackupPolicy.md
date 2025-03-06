# FullBackupPolicy

Specifies full backup settings for a Protection Group. Currently, full backup settings can be specified by using either of 'schedule' or 'schdulesAndRetentions' field. Using 'schdulesAndRetentions' is recommended when multiple full backups need to be configured. If full and incremental backup has common retention then only setting 'schedule' is recommended.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**FullSchedule**](FullSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.full_backup_policy import FullBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FullBackupPolicy from a JSON string
full_backup_policy_instance = FullBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(FullBackupPolicy.to_json())

# convert the object into a dict
full_backup_policy_dict = full_backup_policy_instance.to_dict()
# create an instance of FullBackupPolicy from a dict
full_backup_policy_from_dict = FullBackupPolicy.from_dict(full_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


