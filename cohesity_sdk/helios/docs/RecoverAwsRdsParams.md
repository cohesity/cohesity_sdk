# RecoverAwsRdsParams

Specifies the parameters to recover AWS RDS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRds**](AwsTargetParamsForRecoverRds.md) | Specifies the params for recovering to an AWS target. | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the RDS instances that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of RDS instances. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_aws_rds_params import RecoverAwsRdsParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsParams from a JSON string
recover_aws_rds_params_instance = RecoverAwsRdsParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsParams.to_json())

# convert the object into a dict
recover_aws_rds_params_dict = recover_aws_rds_params_instance.to_dict()
# create an instance of RecoverAwsRdsParams from a dict
recover_aws_rds_params_from_dict = RecoverAwsRdsParams.from_dict(recover_aws_rds_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


