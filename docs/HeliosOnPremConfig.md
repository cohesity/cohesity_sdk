# HeliosOnPremConfig

Params for Helios OnPrem VM Configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the ID of the Cluster. | [optional] [readonly] 
**kubernetes_subnet_cidr** | **str** | Subnet to use for setting up the Kubernetes cluster&#39;s internal network on which Cohesity Helios will run. | 
**name** | **str** | Name of the new Helios OnPrem VM. | 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | [optional] 
**nodes** | [**List[HeliosOnPremVMNode]**](HeliosOnPremVMNode.md) | Specifies the Nodes present in this Cluster. | [optional] 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**ssh_config** | [**HeliosOnPremSSHConfig**](HeliosOnPremSSHConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.helios_on_prem_config import HeliosOnPremConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosOnPremConfig from a JSON string
helios_on_prem_config_instance = HeliosOnPremConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosOnPremConfig.to_json())

# convert the object into a dict
helios_on_prem_config_dict = helios_on_prem_config_instance.to_dict()
# create an instance of HeliosOnPremConfig from a dict
helios_on_prem_config_from_dict = HeliosOnPremConfig.from_dict(helios_on_prem_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


