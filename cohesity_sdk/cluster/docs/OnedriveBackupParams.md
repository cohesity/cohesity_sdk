# OnedriveBackupParams

Specifies OneDrive job parameters applicable for all Office365 Environment type Protection Sources in a Protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path_filter** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**should_backup_onedrive** | **bool** |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.onedrive_backup_params import OnedriveBackupParams

# TODO update the JSON string below
json = "{}"
# create an instance of OnedriveBackupParams from a JSON string
onedrive_backup_params_instance = OnedriveBackupParams.from_json(json)
# print the JSON string representation of the object
print(OnedriveBackupParams.to_json())

# convert the object into a dict
onedrive_backup_params_dict = onedrive_backup_params_instance.to_dict()
# create an instance of OnedriveBackupParams from a dict
onedrive_backup_params_from_dict = OnedriveBackupParams.from_dict(onedrive_backup_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


