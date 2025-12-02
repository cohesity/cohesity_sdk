# RecoverAwsVmParams

Specifies the parameters to recover AWS VM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverVm**](AwsTargetParamsForRecoverVm.md) |  | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_vm_params import RecoverAwsVmParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsVmParams from a JSON string
recover_aws_vm_params_instance = RecoverAwsVmParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsVmParams.to_json())

# convert the object into a dict
recover_aws_vm_params_dict = recover_aws_vm_params_instance.to_dict()
# create an instance of RecoverAwsVmParams from a dict
recover_aws_vm_params_from_dict = RecoverAwsVmParams.from_dict(recover_aws_vm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


