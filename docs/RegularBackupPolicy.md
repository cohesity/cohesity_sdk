# RegularBackupPolicy

Specifies the Incremental and Full policy settings and also the common Retention policy settings.\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full** | [**FullBackupPolicy**](FullBackupPolicy.md) |  | [optional] 
**full_backups** | [**List[FullScheduleAndRetention]**](FullScheduleAndRetention.md) | Specifies multiple schedules and retentions for full backup. Specify either of the &#39;full&#39; or &#39;fullBackups&#39; values. Its recommended to use &#39;fullBaackups&#39; value since &#39;full&#39; will be deprecated after few releases. | [optional] 
**incremental** | [**IncrementalBackupPolicy**](IncrementalBackupPolicy.md) |  | [optional] 
**primary_backup_target** | [**PrimaryBackupTarget**](PrimaryBackupTarget.md) |  | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.regular_backup_policy import RegularBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of RegularBackupPolicy from a JSON string
regular_backup_policy_instance = RegularBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(RegularBackupPolicy.to_json())

# convert the object into a dict
regular_backup_policy_dict = regular_backup_policy_instance.to_dict()
# create an instance of RegularBackupPolicy from a dict
regular_backup_policy_from_dict = RegularBackupPolicy.from_dict(regular_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


