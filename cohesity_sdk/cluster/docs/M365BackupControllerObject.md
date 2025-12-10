# M365BackupControllerObject

Specifies the Service App Info for the Backup Controller for the Cohesity App for against a specific tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_time_secs** | **float** | Specifies the time in Epoch secs from which this App will be or has been the active controller. | [optional] 
**id** | **str** | Specifies the Service App ID of the M365 backup Controller | [optional] 
**registration_time_secs** | **float** | Specifies the Service App registration time in Epoch secs | [optional] 
**status** | **str** | Specifies the Service App status | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.m365_backup_controller_object import M365BackupControllerObject

# TODO update the JSON string below
json = "{}"
# create an instance of M365BackupControllerObject from a JSON string
m365_backup_controller_object_instance = M365BackupControllerObject.from_json(json)
# print the JSON string representation of the object
print(M365BackupControllerObject.to_json())

# convert the object into a dict
m365_backup_controller_object_dict = m365_backup_controller_object_instance.to_dict()
# create an instance of M365BackupControllerObject from a dict
m365_backup_controller_object_from_dict = M365BackupControllerObject.from_dict(m365_backup_controller_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


