# HeliosIncrementalBackupPolicy

Specifies incremental backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**HeliosIncrementalSchedule**](HeliosIncrementalSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_incremental_backup_policy import HeliosIncrementalBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosIncrementalBackupPolicy from a JSON string
helios_incremental_backup_policy_instance = HeliosIncrementalBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosIncrementalBackupPolicy.to_json())

# convert the object into a dict
helios_incremental_backup_policy_dict = helios_incremental_backup_policy_instance.to_dict()
# create an instance of HeliosIncrementalBackupPolicy from a dict
helios_incremental_backup_policy_from_dict = HeliosIncrementalBackupPolicy.from_dict(helios_incremental_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


