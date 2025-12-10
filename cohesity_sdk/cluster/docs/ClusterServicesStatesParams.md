# ClusterServicesStatesParams

Describes the parameters for fetching services states of cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ids** | **List[int]** | List of nodes whose services status is required. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_services_states_params import ClusterServicesStatesParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterServicesStatesParams from a JSON string
cluster_services_states_params_instance = ClusterServicesStatesParams.from_json(json)
# print the JSON string representation of the object
print(ClusterServicesStatesParams.to_json())

# convert the object into a dict
cluster_services_states_params_dict = cluster_services_states_params_instance.to_dict()
# create an instance of ClusterServicesStatesParams from a dict
cluster_services_states_params_from_dict = ClusterServicesStatesParams.from_dict(cluster_services_states_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


