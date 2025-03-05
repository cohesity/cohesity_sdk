# VmwareTargetParamsForRecoverVAppTemplate

Specifies the parameters for a VMware recovery target when recovering a vApp Template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_differential_restore** | **bool** | Specifies whether to attempt differential restore. | [optional] 
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**disk_provision_type** | **str** | Specifies the Virtual Disk Provisioning Policies for Vmware VM | [optional] 
**enable_nbdssl_fallback** | **bool** | If this field is set to true and SAN transport recovery fails, then recovery will fallback to use NBDSSL transport. This field only applies if &#39;leverageSanTransport&#39; is set to true. | [optional] 
**leverage_san_transport** | **bool** | Specifies whether to enable SAN transport for copy recovery or not | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**recovery_target_config** | [**VmwareVAppTemplateRecoveryTargetConfig**](VmwareVAppTemplateRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_v_app_template_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_target_params_for_recover_v_app_template import VmwareTargetParamsForRecoverVAppTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareTargetParamsForRecoverVAppTemplate from a JSON string
vmware_target_params_for_recover_v_app_template_instance = VmwareTargetParamsForRecoverVAppTemplate.from_json(json)
# print the JSON string representation of the object
print(VmwareTargetParamsForRecoverVAppTemplate.to_json())

# convert the object into a dict
vmware_target_params_for_recover_v_app_template_dict = vmware_target_params_for_recover_v_app_template_instance.to_dict()
# create an instance of VmwareTargetParamsForRecoverVAppTemplate from a dict
vmware_target_params_for_recover_v_app_template_from_dict = VmwareTargetParamsForRecoverVAppTemplate.from_dict(vmware_target_params_for_recover_v_app_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


