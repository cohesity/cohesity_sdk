# HeliosBmrSchedule

Specifies settings that defines how frequent bmr backup will be performed for a Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str, none_type** | Specifies how often to start new runs of a Protection Group. &lt;br&gt;&#39;Weeks&#39; specifies that new Protection Group runs start weekly on certain days specified using &#39;dayOfWeek&#39; field. &lt;br&gt;&#39;Months&#39; specifies that new Protection Group runs start monthly on certain day of specific week. | [optional] 
**week_schedule** | [**HeliosWeekSchedule**](HeliosWeekSchedule.md) |  | [optional] 
**month_schedule** | [**HeliosMonthSchedule**](HeliosMonthSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


