# PhysicalTargetParamsForRecoverVolume

Specifies the parameters for a physical recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_unmount_volume** | **bool** | Specifies whether volume would be dismounted first during LockVolume failure. If not specified, default is false. | [optional] 
**mount_target** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the target entity where the volumes are being mounted. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 
**volume_mapping** | [**List[RecoverVolumeMapping]**](RecoverVolumeMapping.md) | Specifies the mapping from source volumes to destination volumes. | 

## Example

```python
from cohesity_sdk.helios.models.physical_target_params_for_recover_volume import PhysicalTargetParamsForRecoverVolume

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalTargetParamsForRecoverVolume from a JSON string
physical_target_params_for_recover_volume_instance = PhysicalTargetParamsForRecoverVolume.from_json(json)
# print the JSON string representation of the object
print(PhysicalTargetParamsForRecoverVolume.to_json())

# convert the object into a dict
physical_target_params_for_recover_volume_dict = physical_target_params_for_recover_volume_instance.to_dict()
# create an instance of PhysicalTargetParamsForRecoverVolume from a dict
physical_target_params_for_recover_volume_from_dict = PhysicalTargetParamsForRecoverVolume.from_dict(physical_target_params_for_recover_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


