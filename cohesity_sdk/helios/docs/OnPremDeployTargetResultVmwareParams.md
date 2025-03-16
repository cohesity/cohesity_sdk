# OnPremDeployTargetResultVmwareParams

Specifies information about a VMware OnPrem deploy target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moref** | [**MOref**](MOref.md) |  | [optional] 
**uuid** | **str** | UUID of the recovered VMware VM | [optional] 

## Example

```python
from cohesity_sdk.helios.models.on_prem_deploy_target_result_vmware_params import OnPremDeployTargetResultVmwareParams

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremDeployTargetResultVmwareParams from a JSON string
on_prem_deploy_target_result_vmware_params_instance = OnPremDeployTargetResultVmwareParams.from_json(json)
# print the JSON string representation of the object
print(OnPremDeployTargetResultVmwareParams.to_json())

# convert the object into a dict
on_prem_deploy_target_result_vmware_params_dict = on_prem_deploy_target_result_vmware_params_instance.to_dict()
# create an instance of OnPremDeployTargetResultVmwareParams from a dict
on_prem_deploy_target_result_vmware_params_from_dict = OnPremDeployTargetResultVmwareParams.from_dict(on_prem_deploy_target_result_vmware_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


