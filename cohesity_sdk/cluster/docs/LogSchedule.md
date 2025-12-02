# LogSchedule

Specifies settings that defines how frequent log backup will be performed for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour_schedule** | [**FrequencySchedule**](FrequencySchedule.md) |  | [optional] 
**minute_schedule** | [**FrequencySchedule**](FrequencySchedule.md) |  | [optional] 
**unit** | **str** | Specifies how often to start new Protection Group Runs of a Protection Group. &lt;br&gt;&#39;Minutes&#39; specifies that Protection Group run starts periodically after certain number of minutes specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Hours&#39; specifies that Protection Group run starts periodically after certain number of hours specified in &#39;frequency&#39; field. | 

## Example

```python
from cohesity_sdk.cluster.models.log_schedule import LogSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of LogSchedule from a JSON string
log_schedule_instance = LogSchedule.from_json(json)
# print the JSON string representation of the object
print(LogSchedule.to_json())

# convert the object into a dict
log_schedule_dict = log_schedule_instance.to_dict()
# create an instance of LogSchedule from a dict
log_schedule_from_dict = LogSchedule.from_dict(log_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


