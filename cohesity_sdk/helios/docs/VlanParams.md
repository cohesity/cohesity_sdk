# VlanParams

Specifies VLAN params associated with the backup/restore operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_vlan** | **bool** | If this is set to true, then even if VLANs are configured on the system, the partition VIPs will be used for the restore. | [optional] 
**interface_name** | **str** | Interface group to use for backup/restore. If this is not specified, primary interface group for the cluster will be used. | [optional] 
**vlan_id** | **int** | If this is set, then the Cohesity host name or the IP address associated with this VLAN is used for mounting Cohesity&#39;s view on the remote host. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vlan_params import VlanParams

# TODO update the JSON string below
json = "{}"
# create an instance of VlanParams from a JSON string
vlan_params_instance = VlanParams.from_json(json)
# print the JSON string representation of the object
print(VlanParams.to_json())

# convert the object into a dict
vlan_params_dict = vlan_params_instance.to_dict()
# create an instance of VlanParams from a dict
vlan_params_from_dict = VlanParams.from_dict(vlan_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


