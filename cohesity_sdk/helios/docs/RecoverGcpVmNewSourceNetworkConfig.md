# RecoverGcpVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for GCP VMs if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet** | [**GcpVpcSubnetConfig**](GcpVpcSubnetConfig.md) | Specifies the subnet. | 

## Example

```python
from cohesity_sdk.helios.models.recover_gcp_vm_new_source_network_config import RecoverGcpVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGcpVmNewSourceNetworkConfig from a JSON string
recover_gcp_vm_new_source_network_config_instance = RecoverGcpVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGcpVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_gcp_vm_new_source_network_config_dict = recover_gcp_vm_new_source_network_config_instance.to_dict()
# create an instance of RecoverGcpVmNewSourceNetworkConfig from a dict
recover_gcp_vm_new_source_network_config_from_dict = RecoverGcpVmNewSourceNetworkConfig.from_dict(recover_gcp_vm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


