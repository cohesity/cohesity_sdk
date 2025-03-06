# RecoverVmwareVAppParams

Specifies the parameters to recover VMware vApp.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vmware_target_params** | [**VmwareTargetParamsForRecoverVApp**](VmwareTargetParamsForRecoverVApp.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_v_app_params import RecoverVmwareVAppParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVAppParams from a JSON string
recover_vmware_v_app_params_instance = RecoverVmwareVAppParams.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVAppParams.to_json())

# convert the object into a dict
recover_vmware_v_app_params_dict = recover_vmware_v_app_params_instance.to_dict()
# create an instance of RecoverVmwareVAppParams from a dict
recover_vmware_v_app_params_from_dict = RecoverVmwareVAppParams.from_dict(recover_vmware_v_app_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


