# RecoverHyperVVmParams

Specifies the parameters to recover VMs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hyperv_target_params** | [**HyperVTargetParamsForRecoverVm**](HyperVTargetParamsForRecoverVm.md) | Specifies the params for recovering to a HyperV target. | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_hyper_vvm_params import RecoverHyperVVmParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmParams from a JSON string
recover_hyper_vvm_params_instance = RecoverHyperVVmParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmParams.to_json())

# convert the object into a dict
recover_hyper_vvm_params_dict = recover_hyper_vvm_params_instance.to_dict()
# create an instance of RecoverHyperVVmParams from a dict
recover_hyper_vvm_params_from_dict = RecoverHyperVVmParams.from_dict(recover_hyper_vvm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


