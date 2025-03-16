# GetProtectionRunProgressBody

Specifies the progress of a protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_run** | [**List[ArchivalTargetProgressInfo]**](ArchivalTargetProgressInfo.md) | Progress for the archival run. | [optional] 
**local_run** | [**BackupRunProgressInfo**](BackupRunProgressInfo.md) |  | [optional] 
**replication_run** | [**List[ReplicationTargetProgressInfo]**](ReplicationTargetProgressInfo.md) | Progress for the replication run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_protection_run_progress_body import GetProtectionRunProgressBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetProtectionRunProgressBody from a JSON string
get_protection_run_progress_body_instance = GetProtectionRunProgressBody.from_json(json)
# print the JSON string representation of the object
print(GetProtectionRunProgressBody.to_json())

# convert the object into a dict
get_protection_run_progress_body_dict = get_protection_run_progress_body_instance.to_dict()
# create an instance of GetProtectionRunProgressBody from a dict
get_protection_run_progress_body_from_dict = GetProtectionRunProgressBody.from_dict(get_protection_run_progress_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


