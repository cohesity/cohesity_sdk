# RecoverAwsAuroraParams

Specifies the parameters to recover AWS Aurora.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverAurora**](AwsTargetParamsForRecoverAurora.md) |  | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the Aurora instances that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of Aurora instances. User has to make sure specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_aws_aurora_params import RecoverAwsAuroraParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsAuroraParams from a JSON string
recover_aws_aurora_params_instance = RecoverAwsAuroraParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsAuroraParams.to_json())

# convert the object into a dict
recover_aws_aurora_params_dict = recover_aws_aurora_params_instance.to_dict()
# create an instance of RecoverAwsAuroraParams from a dict
recover_aws_aurora_params_from_dict = RecoverAwsAuroraParams.from_dict(recover_aws_aurora_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


