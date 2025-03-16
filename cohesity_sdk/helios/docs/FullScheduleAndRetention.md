# FullScheduleAndRetention

Specifies the settings to schedule the full backup and retention for each schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**Retention**](Retention.md) |  | 
**schedule** | [**FullSchedule**](FullSchedule.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.full_schedule_and_retention import FullScheduleAndRetention

# TODO update the JSON string below
json = "{}"
# create an instance of FullScheduleAndRetention from a JSON string
full_schedule_and_retention_instance = FullScheduleAndRetention.from_json(json)
# print the JSON string representation of the object
print(FullScheduleAndRetention.to_json())

# convert the object into a dict
full_schedule_and_retention_dict = full_schedule_and_retention_instance.to_dict()
# create an instance of FullScheduleAndRetention from a dict
full_schedule_and_retention_from_dict = FullScheduleAndRetention.from_dict(full_schedule_and_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


