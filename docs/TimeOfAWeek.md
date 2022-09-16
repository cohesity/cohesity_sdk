# TimeOfAWeek

Specifies a time period by specifying a single daily time period and one or more days of the week, for example 9 AM - 5 PM on Monday, Wednesday or Friday. If different time periods are required on different days, then multiple instances of this Weekly Time Period must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **[str], none_type** | Array of Week Days. Specifies a list of days of a week (such as &#39;Sunday&#39;) when the time period should be applied. If not set, the time range applies to all days of the week. Specifies a day in a week such as &#39;Sunday&#39;, &#39;Monday&#39;, etc. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**end_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**is_all_day** | **bool, none_type** | All Day. Specifies that bandwidth limit is applied for entire day. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


