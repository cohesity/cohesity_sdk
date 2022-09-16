# CommonTdmObjectTimelineEventsResponseParams

Specifies the common parameters for the TDM object timeline events response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique ID of the event. | 
**action** | **str, none_type** | Specifies the action for the event. | 
**created_at** | **int, none_type** | Specifies the time (in usecs from epoch) at which the event was created. | [optional] 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the user, who triggered the event. | [optional] 
**status** | **str, none_type** | Specifies the current status of the event. | [optional] 
**error_message** | **str, none_type** | Specifies the error message if the event is in failed state. | [optional] 
**description** | **str, none_type** | Specifies the description of the event, as provided by the user. | [optional] 
**event_group_id** | **str, none_type** | Specifies the ID of the group this event belongs to. Events with same group ID are considered to be a single timeline for the TDM object. Different group IDs mean different timelines for the TDM object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


