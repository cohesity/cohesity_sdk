# HeliosPolicyRequest

Specifies the request parameters to cretae a policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_policy** | [**HeliosBackupPolicy**](HeliosBackupPolicy.md) |  | [optional] 
**blackout_window** | [**List[HeliosBlackoutWindow]**](HeliosBlackoutWindow.md) | List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**cluster_identifier** | **str** | Specifies the cluster to which this policy belongs. This required is only for type OnPremPolicy. The format is clusterId:clusterIncarnationId. | [optional] 
**data_lock** | **str** | This field is now deprecated. Please use the DataLockConfig in the backup retention. | [optional] 
**description** | **str** | Specifies the description of the Protection Policy. | [optional] 
**extended_retention** | [**List[HeliosExtendedRetentionPolicy]**](HeliosExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**name** | **str** | Specifies the name of the Protection Policy. | 
**remote_target_policy** | [**HeliosTargetsConfiguration**](HeliosTargetsConfiguration.md) |  | [optional] 
**retry_options** | [**HeliosRetryOptions**](HeliosRetryOptions.md) |  | [optional] 
**tenant_ids** | **List[Optional[str]]** | Specifies the tenants which have access to this object. | [optional] [readonly] 
**type** | **str** | Specifies the type of the Protection Policy to be created on Helios. | 

## Example

```python
from cohesity_sdk.helios.models.helios_policy_request import HeliosPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosPolicyRequest from a JSON string
helios_policy_request_instance = HeliosPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(HeliosPolicyRequest.to_json())

# convert the object into a dict
helios_policy_request_dict = helios_policy_request_instance.to_dict()
# create an instance of HeliosPolicyRequest from a dict
helios_policy_request_from_dict = HeliosPolicyRequest.from_dict(helios_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


