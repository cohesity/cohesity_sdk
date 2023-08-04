# ProtectionPolicyResponse

Specifies the details about the Protection Policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Protection Policy. | 
**backup_policy** | [**BackupPolicy**](BackupPolicy.md) |  | 
**description** | **str, none_type** | Specifies the description of the Protection Policy. | [optional] 
**blackout_window** | [**[BlackoutWindow], none_type**](BlackoutWindow.md) | List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**extended_retention** | [**[ExtendedRetentionPolicy], none_type**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**remote_target_policy** | [**TargetsConfiguration**](TargetsConfiguration.md) |  | [optional] 
**cascaded_targets_config** | [**[CascadedTargetConfiguration]**](CascadedTargetConfiguration.md) | Specifies the configuration for cascaded replications. Using cascaded replication, replication cluster(Rx) can further replicate and archive the snapshot copies to further targets. Its recommended to create cascaded configuration where protection group will be created. | [optional] 
**retry_options** | [**RetryOptions**](RetryOptions.md) |  | [optional] 
**data_lock** | **str, none_type** | This field is now deprecated. Please use the DataLockConfig in the backup retention. | [optional] 
**version** | **int, none_type** | Specifies the current policy verison. Policy version is incremented for optionally supporting new features and differentialting across releases. | [optional] 
**is_cbs_enabled** | **bool, none_type** | Specifies true if Calender Based Schedule is supported by client. Default value is assumed as false for this feature. | [optional] 
**id** | **str, none_type** | Specifies a unique Policy id assigned by the Cohesity Cluster. | [optional] 
**template_id** | **str, none_type** | Specifies the parent policy template id to which the policy is linked to. This field is set only when policy is created from template. | [optional] 
**is_usable** | **bool, none_type** | This field is set to true if the linked policy which is internally created from a policy templates qualifies as usable to create more policies on the cluster. If the linked policy is partially filled and can not create a working policy then this field will be set to false. In case of normal policy created on the cluster, this field wont be populated. | [optional] 
**is_replicated** | **bool, none_type** | This field is set to true when policy is the replicated policy. | [optional] 
**num_protection_groups** | **int, none_type** | Specifies the number of protection groups using the protection policy. | [optional] 
**num_protected_objects** | **int, none_type** | Specifies the number of protected objects using the protection policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


