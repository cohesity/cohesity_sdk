# BlackoutWindow

Specifies a time range in a single day when new Protection Group Runs of Protection Groups cannot be started. For example, a Protection Group with a daily schedule could define a blackout period for Sunday.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str, none_type** | Specifies a day in the week when no new Protection Group Runs should be started such as &#39;Sunday&#39;. Specifies a day in a week such as &#39;Sunday&#39;, &#39;Monday&#39;, etc. | 
**end_time** | [**TimeOfDay**](TimeOfDay.md) |  | 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | 
**config_id** | **str, none_type** | Specifies the unique identifier for the target getting added. This field need to be passed olny when policies are updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


