# OutlookBackupParams

Specifies Outlook job parameters applicable for all Office365 Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path_filter** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**should_backup_mailbox** | **bool** |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.outlook_backup_params import OutlookBackupParams

# TODO update the JSON string below
json = "{}"
# create an instance of OutlookBackupParams from a JSON string
outlook_backup_params_instance = OutlookBackupParams.from_json(json)
# print the JSON string representation of the object
print(OutlookBackupParams.to_json())

# convert the object into a dict
outlook_backup_params_dict = outlook_backup_params_instance.to_dict()
# create an instance of OutlookBackupParams from a dict
outlook_backup_params_from_dict = OutlookBackupParams.from_dict(outlook_backup_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


