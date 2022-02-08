# ProtectionPolicyRequest

Specifies the request to create a Protection Policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Protection Policy. | 
**backup_policy** | [**BackupPolicy**](BackupPolicy.md) |  | 
**description** | **str, none_type** | Specifies the description of the Protection Policy. | [optional] 
**blackout_window** | [**[BlackoutWindow], none_type**](BlackoutWindow.md) | List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**extended_retention** | [**[ExtendedRetentionPolicy], none_type**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**remote_target_policy** | [**TargetsConfiguration**](TargetsConfiguration.md) |  | [optional] 
**retry_options** | [**RetryOptions**](RetryOptions.md) |  | [optional] 
**data_lock** | **str, none_type** | This field is now deprecated. Please use the DataLockConfig in the backup retention. | [optional] 
**template_id** | **str, none_type** | Specifies the parent policy template id to which the policy is linked to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


