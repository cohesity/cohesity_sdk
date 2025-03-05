# AwsTargetParamsForRecoverVm

Specifies the parameters for an AWS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**custom_tags** | [**List[SimpleTags]**](SimpleTags.md) | Specifies the custom tags that need to be present on on every temporary and permanent entity that this job creates. | [optional] 
**fleet_config** | [**FleetConfig**](FleetConfig.md) |  | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_target_config** | [**AwsVmRecoveryTargetConfig**](AwsVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_target_params_for_recover_vm import AwsTargetParamsForRecoverVm

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverVm from a JSON string
aws_target_params_for_recover_vm_instance = AwsTargetParamsForRecoverVm.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverVm.to_json())

# convert the object into a dict
aws_target_params_for_recover_vm_dict = aws_target_params_for_recover_vm_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverVm from a dict
aws_target_params_for_recover_vm_from_dict = AwsTargetParamsForRecoverVm.from_dict(aws_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


