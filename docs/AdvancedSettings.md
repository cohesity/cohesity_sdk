# AdvancedSettings

This is used to regulate certain gflag values from the UI. The values passed by the user from the UI will be used for the respective gflags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloned_db_backup_status** | **str** | Whether to report error if SQL database is cloned. | [optional] 
**db_backup_if_not_online_status** | **str** | Whether to report error if SQL database is not online. | [optional] 
**missing_db_backup_status** | **str** | Fail the backup job when the database is missing. The database may be missing if it is deleted or corrupted. | [optional] 
**offline_restoring_db_backup_status** | **str** | Fail the backup job when database is offline or restoring. | [optional] 
**read_only_db_backup_status** | **str** | Whether to skip backup for read-only SQL databases. | [optional] 
**report_all_non_autoprotect_db_errors** | **str** | Whether to report error for all dbs in non-autoprotect jobs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.advanced_settings import AdvancedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedSettings from a JSON string
advanced_settings_instance = AdvancedSettings.from_json(json)
# print the JSON string representation of the object
print(AdvancedSettings.to_json())

# convert the object into a dict
advanced_settings_dict = advanced_settings_instance.to_dict()
# create an instance of AdvancedSettings from a dict
advanced_settings_from_dict = AdvancedSettings.from_dict(advanced_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


