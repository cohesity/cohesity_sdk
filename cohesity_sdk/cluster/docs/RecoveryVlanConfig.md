# RecoveryVlanConfig

Specifies the VLAN configuration for Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_vlan** | **bool** | If this is set to true, then even if VLANs are configured on the system, the partition VIPs will be used for the Recovery. | [optional] 
**id** | **int** | If this is set, then the Cohesity host name or the IP address associated with this vlan is used for mounting Cohesity&#39;s view on the remote host. | [optional] 
**interface_name** | **str** | Interface group to use for Recovery. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryVlanConfig from a JSON string
recovery_vlan_config_instance = RecoveryVlanConfig.from_json(json)
# print the JSON string representation of the object
print(RecoveryVlanConfig.to_json())

# convert the object into a dict
recovery_vlan_config_dict = recovery_vlan_config_instance.to_dict()
# create an instance of RecoveryVlanConfig from a dict
recovery_vlan_config_from_dict = RecoveryVlanConfig.from_dict(recovery_vlan_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


