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
**recovery_target_config** | [**VmwareVAppTemplateRecoveryTargetConfig**](VmwareVAppTemplateRecoveryTargetConfig.md) | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source or to original Source with different configuration. If not specified, then the recovery of the vApp templates will be performed to original location with all configuration parameters retained. | [optional] 
**rename_recovered_v_app_template_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) | Specifies params to rename the vApps templates that are recovered. If not specified, the original names of the vApp templates are preserved. | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) | Specifies params to rename the VMs that are recovered. If not specified, the original names of the VMs are preserved. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_target_params_for_recover_v_app_template import VmwareTargetParamsForRecoverVAppTemplate

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


