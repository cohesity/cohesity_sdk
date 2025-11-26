# HeliosFullSchedule

Specifies settings that defines how frequent full backup will be performed for a Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_schedule** | [**HeliosDaySchedule**](HeliosDaySchedule.md) |  | [optional] 
**month_schedule** | [**HeliosMonthSchedule**](HeliosMonthSchedule.md) |  | [optional] 
**unit** | **str, none_type** | Specifies how often to start new runs of a Protection Group. &lt;br&gt;&#39;Days&#39; specifies that Protection Group run starts periodically on every day. For full backup schedule, currently we only support frequecny of 1 which indicates that full backup will be performed daily. &lt;br&gt;&#39;Weeks&#39; specifies that new Protection Group runs start weekly on certain days specified using &#39;dayOfWeek&#39; field. &lt;br&gt;&#39;Months&#39; specifies that new Protection Group runs start monthly on certain day of specific week. This schedule needs &#39;weekOfMonth&#39; and &#39;dayOfWeek&#39; fields to be set. &lt;br&gt;&#39;ProtectOnce&#39; specifies that groups using this policy option will run only once and after that group will permanently be disabled. &lt;br&gt; Example: To run the Protection Group on Second Sunday of Every Month, following schedule need to be set: &lt;br&gt; unit: &#39;Month&#39; &lt;br&gt; dayOfWeek: &#39;Sunday&#39; &lt;br&gt; weekOfMonth: &#39;Second&#39; | [optional] 
**week_schedule** | [**HeliosWeekSchedule**](HeliosWeekSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


