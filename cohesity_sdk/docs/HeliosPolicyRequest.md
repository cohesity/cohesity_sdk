# HeliosPolicyRequest

Specifies the request parameters to cretae a policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Protection Policy. | 
**type** | **str, none_type** | Specifies the type of the Protection Policy to be created on Helios. | 
**cluster_identifier** | **str, none_type** | Specifies the cluster to which this policy belongs. This required is only for type OnPremPolicy. The format is clusterId:clusterIncarnationId. | [optional] 
**tenant_ids** | **[str, none_type]** | Specifies the tenants which have access to this object. | [optional] [readonly] 
**backup_policy** | [**HeliosBackupPolicy**](HeliosBackupPolicy.md) |  | [optional] 
**description** | **str, none_type** | Specifies the description of the Protection Policy. | [optional] 
**blackout_window** | [**[HeliosBlackoutWindow], none_type**](HeliosBlackoutWindow.md) | List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**extended_retention** | [**[HeliosExtendedRetentionPolicy], none_type**](HeliosExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**remote_target_policy** | [**HeliosTargetsConfiguration**](HeliosTargetsConfiguration.md) |  | [optional] 
**retry_options** | [**HeliosRetryOptions**](HeliosRetryOptions.md) |  | [optional] 
**data_lock** | **str, none_type** | This field is now deprecated. Please use the DataLockConfig in the backup retention. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


