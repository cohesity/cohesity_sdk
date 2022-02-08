# RecoverAwsAuroraParams

Specifies the parameters to recover AWS Aurora.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**recover_protection_group_runs_params** | [**[RecoverProtectionGroupRunParams], none_type**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the Aurora instances that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of Aurora instances. User has to make sure specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**aws_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for recovering to an AWS target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


