# TargetSchedule

Specifies a schedule fregquency and schedule unit for copying Snapshots to backup targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Specifies a factor to multiply the unit by, to determine the copy schedule. For example if set to 2 and the unit is hourly, then Snapshots from the first eligible Job Run for every 2 hour period is copied. | [optional] 
**unit** | **str** | Specifies the frequency that Snapshots should be copied to the specified target. Used in combination with multiplier. &lt;br&gt;&#39;Runs&#39; means that the Snapshot copy occurs after the number of Protection Group Runs equals the number specified in the frequency. &lt;br&gt;&#39;Hours&#39; means that the Snapshot copy occurs hourly at the frequency set in the frequency, for example if scheduleFrequency is 2, the copy occurs every 2 hours. &lt;br&gt;&#39;Days&#39; means that the Snapshot copy occurs daily at the frequency set in the frequency. &lt;br&gt;&#39;Weeks&#39; means that the Snapshot copy occurs weekly at the frequency set in the frequency. &lt;br&gt;&#39;Months&#39; means that the Snapshot copy occurs monthly at the frequency set in the Frequency. &lt;br&gt;&#39;Years&#39; means that the Snapshot copy occurs yearly at the frequency set in the scheduleFrequency. | 

## Example

```python
from cohesity_sdk.cluster.models.target_schedule import TargetSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TargetSchedule from a JSON string
target_schedule_instance = TargetSchedule.from_json(json)
# print the JSON string representation of the object
print(TargetSchedule.to_json())

# convert the object into a dict
target_schedule_dict = target_schedule_instance.to_dict()
# create an instance of TargetSchedule from a dict
target_schedule_from_dict = TargetSchedule.from_dict(target_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


