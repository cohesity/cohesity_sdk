# ProtectionPolicy

Specifies common fields required to define Protection Policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_policy** | [**BackupPolicy**](BackupPolicy.md) |  | 
**name** | **str, none_type** | Specifies the name of the Protection Policy. | 
**blackout_window** | [**[BlackoutWindow], none_type**](BlackoutWindow.md) | List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**cascaded_targets_config** | [**[CascadedTargetConfiguration]**](CascadedTargetConfiguration.md) | Specifies the configuration for cascaded replications. Using cascaded replication, replication cluster(Rx) can further replicate and archive the snapshot copies to further targets. Its recommended to create cascaded configuration where protection group will be created. | [optional] 
**data_lock** | **str, none_type** | This field is now deprecated. Please use the DataLockConfig in the backup retention. | [optional] 
**description** | **str, none_type** | Specifies the description of the Protection Policy. | [optional] 
**enable_smart_local_retention_adjustment** | **bool, none_type** | Specifies whether smart local retention adjustment is enabled or not. If enabled, local retention would be extended upon failure of any outgoing replications or archivals. Later, if manual intervention causes the failed copies to succeed, retention would automatically be reduced. | [optional] 
**extended_retention** | [**[ExtendedRetentionPolicy], none_type**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**is_cbs_enabled** | **bool, none_type** | Specifies true if Calender Based Schedule is supported by client. Default value is assumed as false for this feature. | [optional] 
**last_modification_time_usecs** | **int, none_type** | Specifies the last time this Policy was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the policy was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error. | [optional] 
**remote_target_policy** | [**TargetsConfiguration**](TargetsConfiguration.md) |  | [optional] 
**retry_options** | [**RetryOptions**](RetryOptions.md) |  | [optional] 
**rpo_policy_settings** | [**RpoPolicySettings**](RpoPolicySettings.md) |  | [optional] 
**skip_interval_mins** | **int, none_type** | Specifies the period of time before skipping the execution of new group Runs if an existing queued group Run of the same Protection group has not started. For example if this field is set to 30 minutes and a group Run is scheduled to start at 5:00 AM every day but does not start due to conflicts (such as too many groups are running). If the new group Run does not start by 5:30AM, the Cohesity Cluster will skip the new group Run. If the original group Run completes before 5:30AM the next day, a new group Run is created and starts executing. This field is optional. | [optional] 
**version** | **int, none_type** | Specifies the current policy verison. Policy version is incremented for optionally supporting new features and differentialting across releases. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


