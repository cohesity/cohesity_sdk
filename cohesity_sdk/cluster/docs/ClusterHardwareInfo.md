# ClusterHardwareInfo

Specifies a hardware type for motherboard of the nodes that make dnsServerIps this Cohesity Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_models** | **List[str]** |  | [optional] 
**hardware_vendors** | **List[str]** |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_hardware_info import ClusterHardwareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHardwareInfo from a JSON string
cluster_hardware_info_instance = ClusterHardwareInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterHardwareInfo.to_json())

# convert the object into a dict
cluster_hardware_info_dict = cluster_hardware_info_instance.to_dict()
# create an instance of ClusterHardwareInfo from a dict
cluster_hardware_info_from_dict = ClusterHardwareInfo.from_dict(cluster_hardware_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


