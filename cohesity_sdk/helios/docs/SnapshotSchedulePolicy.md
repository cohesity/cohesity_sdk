# SnapshotSchedulePolicy

Describes the snapshot schedule policy struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_month** | **List[int]** | Days of the month. | [optional] 
**days_of_week** | **List[str]** | Days of the week. | [optional] 
**suspended** | **bool** | Bool to denote if the policy is suspended. | [optional] 
**time** | **str** | Time of the day. | [optional] 
**time_zone** | **str** | Time zone. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snapshot_schedule_policy import SnapshotSchedulePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotSchedulePolicy from a JSON string
snapshot_schedule_policy_instance = SnapshotSchedulePolicy.from_json(json)
# print the JSON string representation of the object
print(SnapshotSchedulePolicy.to_json())

# convert the object into a dict
snapshot_schedule_policy_dict = snapshot_schedule_policy_instance.to_dict()
# create an instance of SnapshotSchedulePolicy from a dict
snapshot_schedule_policy_from_dict = SnapshotSchedulePolicy.from_dict(snapshot_schedule_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


