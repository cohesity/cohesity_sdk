# CdpLocalBackupInfo

Specifies the last local backup information for a given CDP object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_in_usecs** | **int** | Specifies the end time of the last local backup taken. | [optional] 
**start_time_in_usecs** | **int** | Specifies the start time of the last local backup taken. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cdp_local_backup_info import CdpLocalBackupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CdpLocalBackupInfo from a JSON string
cdp_local_backup_info_instance = CdpLocalBackupInfo.from_json(json)
# print the JSON string representation of the object
print(CdpLocalBackupInfo.to_json())

# convert the object into a dict
cdp_local_backup_info_dict = cdp_local_backup_info_instance.to_dict()
# create an instance of CdpLocalBackupInfo from a dict
cdp_local_backup_info_from_dict = CdpLocalBackupInfo.from_dict(cdp_local_backup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


