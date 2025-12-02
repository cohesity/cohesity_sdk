# NodeServicesStates

Lists node services states

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies an optional message describing details of the cluster services states. | [optional] 
**node_id** | **int** | Specifies the id of the node. | [optional] 
**node_ips** | **List[str]** | If the node is not part of any cluster, it returns list of local IPs; otherwise it returns the local IP that matches the cluster subnet. | [optional] 
**node_sw_version** | **str** | Node Software Version | [optional] 
**part_of_cluster** | **bool** | Specifies weather node is part of a cluster  | [optional] 
**services_state** | [**List[ServiceState]**](ServiceState.md) | Contains node services states | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_services_states import NodeServicesStates

# TODO update the JSON string below
json = "{}"
# create an instance of NodeServicesStates from a JSON string
node_services_states_instance = NodeServicesStates.from_json(json)
# print the JSON string representation of the object
print(NodeServicesStates.to_json())

# convert the object into a dict
node_services_states_dict = node_services_states_instance.to_dict()
# create an instance of NodeServicesStates from a dict
node_services_states_from_dict = NodeServicesStates.from_dict(node_services_states_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


