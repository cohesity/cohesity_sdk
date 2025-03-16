# HeliosIncrementalSchedule

Specifies settings that defines how frequent backup will be performed for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_schedule** | [**HeliosDaySchedule**](HeliosDaySchedule.md) |  | [optional] 
**hour_schedule** | [**HeliosHourSchedule**](HeliosHourSchedule.md) |  | [optional] 
**minute_schedule** | [**HeliosMinuteSchedule**](HeliosMinuteSchedule.md) |  | [optional] 
**month_schedule** | [**HeliosMonthSchedule**](HeliosMonthSchedule.md) |  | [optional] 
**unit** | **str** | Specifies how often to start new runs of a Protection Group. &lt;br&gt;&#39;Minutes&#39; specifies that Protection Group run starts periodically after certain number of minutes specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Hours&#39; specifies that Protection Group run starts periodically after certain number of hours specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Days&#39; specifies that Protection Group run starts periodically after certain number of days specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Week&#39; specifies that new Protection Group runs start weekly on certain days specified using &#39;dayOfWeek&#39; field. &lt;br&gt;&#39;Month&#39; specifies that new Protection Group runs start monthly on certain day of specific week. This schedule needs &#39;weekOfMonth&#39; and &#39;dayOfWeek&#39; fields to be set. &lt;br&gt; Example: To run the Protection Group on Second Sunday of Every Month, following schedule need to be set: &lt;br&gt; unit: &#39;Month&#39; &lt;br&gt; dayOfWeek: &#39;Sunday&#39; &lt;br&gt; weekOfMonth: &#39;Second&#39; | 
**week_schedule** | [**HeliosWeekSchedule**](HeliosWeekSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_incremental_schedule import HeliosIncrementalSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosIncrementalSchedule from a JSON string
helios_incremental_schedule_instance = HeliosIncrementalSchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosIncrementalSchedule.to_json())

# convert the object into a dict
helios_incremental_schedule_dict = helios_incremental_schedule_instance.to_dict()
# create an instance of HeliosIncrementalSchedule from a dict
helios_incremental_schedule_from_dict = HeliosIncrementalSchedule.from_dict(helios_incremental_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


