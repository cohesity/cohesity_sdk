# PauseMetadata

Encapsulation of all pause related data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_pause_modification_time_usecs** | **int, none_type** | Time in usec when the job was last paused or unpaused. | [optional] 
**last_paused_by_username** | **str, none_type** | The user who last paused this protection group. | [optional] 
**paused_note** | **str, none_type** | A note from the user explaining the reason for pausing future runs, if applicable. | [optional] 
**user_initiated_pause_requested_time_usecs** | **int, none_type** | Time in usec when user initiates protection run pause. This field gets populated on user initiated pause and gets cleared on user initiated resume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


