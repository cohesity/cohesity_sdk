# PerformActionOnProtectionGroupRunRequest

Specifies the request to perform actions on protection runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str, none_type** | Specifies the type of the action which will be performed on protection runs. | 
**pause_params** | [**[PauseProtectionRunActionParams]**](PauseProtectionRunActionParams.md) | Specifies the pause action params for a protection run. | [optional] 
**resume_params** | [**[ResumeProtectionRunActionParams]**](ResumeProtectionRunActionParams.md) | Specifies the resume action params for a protection run. | [optional] 
**cancel_params** | [**[CancelProtectionGroupRunRequest]**](CancelProtectionGroupRunRequest.md) | Specifies the cancel action params for a protection run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


