# PrimaryBackupTarget

Specifies the primary backup target settings for regular backups. If the backup target field is not specified then backup will be taken locally on the Cohesity cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_settings** | [**PrimaryArchivalTarget**](PrimaryArchivalTarget.md) |  | [optional] 
**target_type** | **str** | Specifies the primary backup location where backups will be stored. If not specified, then default is assumed as local backup on Cohesity cluster. | [optional] [default to 'Local']

## Example

```python
from cohesity_sdk.models.primary_backup_target import PrimaryBackupTarget

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryBackupTarget from a JSON string
primary_backup_target_instance = PrimaryBackupTarget.from_json(json)
# print the JSON string representation of the object
print(PrimaryBackupTarget.to_json())

# convert the object into a dict
primary_backup_target_dict = primary_backup_target_instance.to_dict()
# create an instance of PrimaryBackupTarget from a dict
primary_backup_target_from_dict = PrimaryBackupTarget.from_dict(primary_backup_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


