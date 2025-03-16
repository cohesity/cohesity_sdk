# DataTieringSchedule

Specifies the data tiering schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_schedule** | [**DaySchedule**](DaySchedule.md) |  | [optional] 
**month_schedule** | [**MonthSchedule**](MonthSchedule.md) |  | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**unit** | **str** | Specifies how often to migrate data from source to target | [optional] 
**week_schedule** | [**WeekSchedule**](WeekSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.data_tiering_schedule import DataTieringSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringSchedule from a JSON string
data_tiering_schedule_instance = DataTieringSchedule.from_json(json)
# print the JSON string representation of the object
print(DataTieringSchedule.to_json())

# convert the object into a dict
data_tiering_schedule_dict = data_tiering_schedule_instance.to_dict()
# create an instance of DataTieringSchedule from a dict
data_tiering_schedule_from_dict = DataTieringSchedule.from_dict(data_tiering_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


