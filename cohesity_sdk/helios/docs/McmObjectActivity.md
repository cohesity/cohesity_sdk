# McmObjectActivity

Specifies the Object activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_run_params** | [**McmObjectArchivalRunActivityParams**](McmObjectArchivalRunActivityParams.md) |  | [optional] 
**backup_run_params** | [**McmObjectBackupRunActivityParams**](McmObjectBackupRunActivityParams.md) |  | [optional] 
**cluster_id** | **int** | Specifies the cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] [readonly] 
**id** | **str** | Specifies the unique id of the activity event. | [optional] 
**object** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**recovery_params** | [**McmObjectRecoverActivityParams**](McmObjectRecoverActivityParams.md) |  | [optional] 
**region_id** | **str** | Specifies the region id. Applicable only in case of DMaaS. | [optional] [readonly] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**timestamp_usecs** | **int** | Specifies the timestamp in Unix timestamp epoch in microseconds at which this activity occured. | [optional] 
**type** | **str** | Specifies the type of activity event. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_activity import McmObjectActivity

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectActivity from a JSON string
mcm_object_activity_instance = McmObjectActivity.from_json(json)
# print the JSON string representation of the object
print(McmObjectActivity.to_json())

# convert the object into a dict
mcm_object_activity_dict = mcm_object_activity_instance.to_dict()
# create an instance of McmObjectActivity from a dict
mcm_object_activity_from_dict = McmObjectActivity.from_dict(mcm_object_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


