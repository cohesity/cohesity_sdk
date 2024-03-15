# ProtectionGroupAlertingPolicy

Specifies a policy for alerting users of the status of a Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_run_status** | **[str]** | Specifies the run status for which the user would like to receive alerts. | 
**alert_targets** | [**[AlertTarget]**](AlertTarget.md) | Specifies a list of targets to receive the alerts. | [optional] 
**raise_object_level_failure_alert** | **bool** | Specifies whether object level alerts are raised for backup failures after the backup run. | [optional] 
**raise_object_level_failure_alert_after_each_attempt** | **bool** | Specifies whether object level alerts are raised for backup failures after each backup attempt. | [optional] 
**raise_object_level_failure_alert_after_last_attempt** | **bool** | Specifies whether object level alerts are raised for backup failures after last backup attempt. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


