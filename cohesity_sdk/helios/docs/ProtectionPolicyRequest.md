# ProtectionPolicyRequest

Specifies the request to create a Protection Policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_policy** | [**BackupPolicy**](BackupPolicy.md) |  | 
**blackout_window** | [**List[BlackoutWindow]**](BlackoutWindow.md) | List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**cascaded_targets_config** | [**List[CascadedTargetConfiguration]**](CascadedTargetConfiguration.md) | Specifies the configuration for cascaded replications. Using cascaded replication, replication cluster(Rx) can further replicate and archive the snapshot copies to further targets. Its recommended to create cascaded configuration where protection group will be created. | [optional] 
**data_lock** | **str** | This field is now deprecated. Please use the DataLockConfig in the backup retention. | [optional] 
**description** | **str** | Specifies the description of the Protection Policy. | [optional] 
**enable_smart_local_retention_adjustment** | **bool** | Specifies whether smart local retention adjustment is enabled or not. If enabled, local retention would be extended upon failure of any outgoing replications or archivals. Later, if manual intervention causes the failed copies to succeed, retention would automatically be reduced. | [optional] 
**extended_retention** | [**List[ExtendedRetentionPolicy]**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**is_cbs_enabled** | **bool** | Specifies true if Calender Based Schedule is supported by client. Default value is assumed as false for this feature. | [optional] 
**last_modification_time_usecs** | **int** | Specifies the last time this Policy was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the policy was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error. | [optional] 
**name** | **str** | Specifies the name of the Protection Policy. | 
**remote_target_policy** | [**TargetsConfiguration**](TargetsConfiguration.md) |  | [optional] 
**retry_options** | [**RetryOptions**](RetryOptions.md) |  | [optional] 
**version** | **int** | Specifies the current policy verison. Policy version is incremented for optionally supporting new features and differentialting across releases. | [optional] 
**template_id** | **str** | Specifies the parent policy template id to which the policy is linked to. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_policy_request import ProtectionPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionPolicyRequest from a JSON string
protection_policy_request_instance = ProtectionPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(ProtectionPolicyRequest.to_json())

# convert the object into a dict
protection_policy_request_dict = protection_policy_request_instance.to_dict()
# create an instance of ProtectionPolicyRequest from a dict
protection_policy_request_from_dict = ProtectionPolicyRequest.from_dict(protection_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


