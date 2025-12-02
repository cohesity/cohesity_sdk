# ClusterIpmiLanInfo

Specifies the cluster ipmi lan info for the cluster in which current node is present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_gateway** | **str** | Specifies the gateway for the given cluster ipmi lan. | [optional] 
**cluster_ipmi_subnet_mask** | **str** | Specifies the subnet mask for the given cluster ipmi lan. | [optional] 
**node_ipmi_entries** | [**List[NodeIpmiInfoEntry]**](NodeIpmiInfoEntry.md) | Specifies the list of node ipmi info for all the nodes in the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_ipmi_lan_info import ClusterIpmiLanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterIpmiLanInfo from a JSON string
cluster_ipmi_lan_info_instance = ClusterIpmiLanInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterIpmiLanInfo.to_json())

# convert the object into a dict
cluster_ipmi_lan_info_dict = cluster_ipmi_lan_info_instance.to_dict()
# create an instance of ClusterIpmiLanInfo from a dict
cluster_ipmi_lan_info_from_dict = ClusterIpmiLanInfo.from_dict(cluster_ipmi_lan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


