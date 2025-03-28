# PolicyTemplateResponse

Specifies the details about the Protection Policy.

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
**id** | **str** | Specifies a unique Policy id assigned by the Cohesity Cluster. | [optional] 
**is_usable** | **bool** | This field is set to true if this policy template qualifies to create more policies. If the template is partially filled and can not create a working policy then this field will be set to false. | [optional] 
**num_linked_policies** | **int** | Specifies the number of policies linked to this policy template. Only applicable in case of policy template. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.policy_template_response import PolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateResponse from a JSON string
policy_template_response_instance = PolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateResponse.to_json())

# convert the object into a dict
policy_template_response_dict = policy_template_response_instance.to_dict()
# create an instance of PolicyTemplateResponse from a dict
policy_template_response_from_dict = PolicyTemplateResponse.from_dict(policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


