# McmProtectionGroupActivity

Specifies the Protection Group activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_run_params** | [**McmProtectionGroupArchivalRunActivityParams**](McmProtectionGroupArchivalRunActivityParams.md) |  | [optional] 
**backup_run_params** | [**McmProtectionGroupBackupRunActivityParams**](McmProtectionGroupBackupRunActivityParams.md) |  | [optional] 
**cluster_id** | **int** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**cluster_name** | **str** | Specifies the cluster name. | [optional] 
**id** | **str** | Specifies the unique id of the activity event. | [optional] 
**policy_id** | **str** | Specifies the Protection Policy Id. | [optional] 
**policy_name** | **str** | Specifies the Protection Policy Name. | [optional] 
**protection_group_id** | **str** | Specifies the Protection Group Id. | [optional] 
**protection_group_name** | **str** | Specifies the Protection Group name. | [optional] 
**region_id** | **str** | Specifies the region id. | [optional] [readonly] 
**run_id** | **str** | Specifies the ID of the Protection Run. | [optional] 
**timestamp_usecs** | **int** | Specifies the timestamp in Unix timestamp epoch in microseconds at which this activity occured. | [optional] 
**type** | **str** | Specifies the type of activity event. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_protection_group_activity import McmProtectionGroupActivity

# TODO update the JSON string below
json = "{}"
# create an instance of McmProtectionGroupActivity from a JSON string
mcm_protection_group_activity_instance = McmProtectionGroupActivity.from_json(json)
# print the JSON string representation of the object
print(McmProtectionGroupActivity.to_json())

# convert the object into a dict
mcm_protection_group_activity_dict = mcm_protection_group_activity_instance.to_dict()
# create an instance of McmProtectionGroupActivity from a dict
mcm_protection_group_activity_from_dict = McmProtectionGroupActivity.from_dict(mcm_protection_group_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


