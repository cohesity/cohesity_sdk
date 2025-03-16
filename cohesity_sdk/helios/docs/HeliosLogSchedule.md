# HeliosLogSchedule

Specifies settings that defines how frequent log backup will be performed for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour_schedule** | [**HeliosHourSchedule**](HeliosHourSchedule.md) |  | [optional] 
**minute_schedule** | [**HeliosMinuteSchedule**](HeliosMinuteSchedule.md) |  | [optional] 
**unit** | **str** | Specifies how often to start new Protection Group Runs of a Protection Group. &lt;br&gt;&#39;Minutes&#39; specifies that Protection Group run starts periodically after certain number of minutes specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Hours&#39; specifies that Protection Group run starts periodically after certain number of hours specified in &#39;frequency&#39; field. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_log_schedule import HeliosLogSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosLogSchedule from a JSON string
helios_log_schedule_instance = HeliosLogSchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosLogSchedule.to_json())

# convert the object into a dict
helios_log_schedule_dict = helios_log_schedule_instance.to_dict()
# create an instance of HeliosLogSchedule from a dict
helios_log_schedule_from_dict = HeliosLogSchedule.from_dict(helios_log_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


