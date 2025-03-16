# HeliosFullBackupPolicy

Specifies full backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**HeliosFullSchedule**](HeliosFullSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_full_backup_policy import HeliosFullBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosFullBackupPolicy from a JSON string
helios_full_backup_policy_instance = HeliosFullBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosFullBackupPolicy.to_json())

# convert the object into a dict
helios_full_backup_policy_dict = helios_full_backup_policy_instance.to_dict()
# create an instance of HeliosFullBackupPolicy from a dict
helios_full_backup_policy_from_dict = HeliosFullBackupPolicy.from_dict(helios_full_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


