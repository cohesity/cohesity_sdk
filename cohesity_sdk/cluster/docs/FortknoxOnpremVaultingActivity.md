# FortknoxOnpremVaultingActivity

Specifies the Fortknox Onprem vaulting activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | Policy ID of the Protection Group on the current cluster. For replication runs, the replicated policy on the Vault cluster shares the same ID as the policy on the Primary cluster. | [optional] 
**policy_name** | **str** | Name of the policy of the Protection Group on the primary cluster. | [optional] 
**protection_environment_type** | **str** | Specifies the type of protection environment. | [optional] 
**protection_group_id** | **str** | Protection Group Id to which this run belongs on current cluster. | [optional] 
**protection_group_name** | **str** | Name of the Protection Group to which this run belongs on current cluster. | [optional] 
**replication_info** | [**FortknoxOnpremVaultingActivityReplicaInfo**](FortknoxOnpremVaultingActivityReplicaInfo.md) |  | [optional] 
**run_id** | **str** | Specifies the ID of the Protection Group run. | [optional] 
**run_start_time_usecs** | **int** | Specifies the start time of run in Unix epoch Timestamp(in microseconds). | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fortknox_onprem_vaulting_activity import FortknoxOnpremVaultingActivity

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxOnpremVaultingActivity from a JSON string
fortknox_onprem_vaulting_activity_instance = FortknoxOnpremVaultingActivity.from_json(json)
# print the JSON string representation of the object
print(FortknoxOnpremVaultingActivity.to_json())

# convert the object into a dict
fortknox_onprem_vaulting_activity_dict = fortknox_onprem_vaulting_activity_instance.to_dict()
# create an instance of FortknoxOnpremVaultingActivity from a dict
fortknox_onprem_vaulting_activity_from_dict = FortknoxOnpremVaultingActivity.from_dict(fortknox_onprem_vaulting_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


