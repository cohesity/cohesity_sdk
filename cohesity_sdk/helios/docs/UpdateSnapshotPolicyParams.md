# UpdateSnapshotPolicyParams

Describes update snapshot policy request params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_month** | **List[int]** | Days of the month. | [optional] 
**days_of_week** | **List[str]** | Days of the week. | [optional] 
**num_of_days_to_keep** | **int** | Number of days to keep the snapshot. | [optional] 
**num_of_versions_to_keep** | **int** | Number of snapshot versions to keep. | [optional] 
**suspend_retention_policy** | **bool** | Suspend snapshot retention policy. | [optional] 
**suspend_schedule_policy** | **bool** | Suspend snapshot schedule policy. | [optional] 
**time** | **str** | Time of the day. | [optional] 
**time_zone** | **str** | Time zone. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_snapshot_policy_params import UpdateSnapshotPolicyParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotPolicyParams from a JSON string
update_snapshot_policy_params_instance = UpdateSnapshotPolicyParams.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotPolicyParams.to_json())

# convert the object into a dict
update_snapshot_policy_params_dict = update_snapshot_policy_params_instance.to_dict()
# create an instance of UpdateSnapshotPolicyParams from a dict
update_snapshot_policy_params_from_dict = UpdateSnapshotPolicyParams.from_dict(update_snapshot_policy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


