# ClusterServicesStates

Lists cluster services states

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**message** | **str** | Specifies an optional message describing details of the cluster services states. | [optional] 
**node_services_states** | [**List[NodeServicesStates]**](NodeServicesStates.md) | lists node-wise services states | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_services_states import ClusterServicesStates

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterServicesStates from a JSON string
cluster_services_states_instance = ClusterServicesStates.from_json(json)
# print the JSON string representation of the object
print(ClusterServicesStates.to_json())

# convert the object into a dict
cluster_services_states_dict = cluster_services_states_instance.to_dict()
# create an instance of ClusterServicesStates from a dict
cluster_services_states_from_dict = ClusterServicesStates.from_dict(cluster_services_states_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


