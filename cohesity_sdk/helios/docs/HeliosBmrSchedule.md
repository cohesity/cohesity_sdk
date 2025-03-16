# HeliosBmrSchedule

Specifies settings that defines how frequent bmr backup will be performed for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month_schedule** | [**HeliosMonthSchedule**](HeliosMonthSchedule.md) |  | [optional] 
**unit** | **str** | Specifies how often to start new runs of a Protection Group. &lt;br&gt;&#39;Weeks&#39; specifies that new Protection Group runs start weekly on certain days specified using &#39;dayOfWeek&#39; field. &lt;br&gt;&#39;Months&#39; specifies that new Protection Group runs start monthly on certain day of specific week. | [optional] 
**week_schedule** | [**HeliosWeekSchedule**](HeliosWeekSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_bmr_schedule import HeliosBmrSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosBmrSchedule from a JSON string
helios_bmr_schedule_instance = HeliosBmrSchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosBmrSchedule.to_json())

# convert the object into a dict
helios_bmr_schedule_dict = helios_bmr_schedule_instance.to_dict()
# create an instance of HeliosBmrSchedule from a dict
helios_bmr_schedule_from_dict = HeliosBmrSchedule.from_dict(helios_bmr_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


