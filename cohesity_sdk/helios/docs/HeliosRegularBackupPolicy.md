# HeliosRegularBackupPolicy

Specifies the Incremental and Full policy settings and also the common Retention policy settings.\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full** | [**HeliosFullBackupPolicy**](HeliosFullBackupPolicy.md) |  | [optional] 
**incremental** | [**HeliosIncrementalBackupPolicy**](HeliosIncrementalBackupPolicy.md) |  | [optional] 
**primary_backup_target** | [**HeliosPrimaryBackupTarget**](HeliosPrimaryBackupTarget.md) |  | [optional] 
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_regular_backup_policy import HeliosRegularBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosRegularBackupPolicy from a JSON string
helios_regular_backup_policy_instance = HeliosRegularBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosRegularBackupPolicy.to_json())

# convert the object into a dict
helios_regular_backup_policy_dict = helios_regular_backup_policy_instance.to_dict()
# create an instance of HeliosRegularBackupPolicy from a dict
helios_regular_backup_policy_from_dict = HeliosRegularBackupPolicy.from_dict(helios_regular_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


