# FortknoxOnpremVaultingActivity

Specifies the Fortknox Onprem vaulting activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str, none_type** | Policy ID of the Protection Group on the current cluster. For replication runs, the replicated policy on the Vault cluster shares the same ID as the policy on the Primary cluster. | [optional] 
**policy_name** | **str, none_type** | Name of the policy of the Protection Group on the primary cluster. | [optional] 
**protection_environment_type** | **str, none_type** | Specifies the type of protection environment. | [optional] 
**protection_group_id** | **str, none_type** | Protection Group Id to which this run belongs on current cluster. | [optional] 
**protection_group_name** | **str, none_type** | Name of the Protection Group to which this run belongs on current cluster. | [optional] 
**replication_info** | [**FortknoxOnpremVaultingActivityReplicaInfo**](FortknoxOnpremVaultingActivityReplicaInfo.md) |  | [optional] 
**run_id** | **str, none_type** | Specifies the ID of the Protection Group run. | [optional] 
**run_start_time_usecs** | **int, none_type** | Specifies the start time of run in Unix epoch Timestamp(in microseconds). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


