# ClusterInterfaces

Specifies the interfaces present on a Cluster grouped by the Node where they are present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[NodeInterfaces]**](NodeInterfaces.md) | Specifies the list of nodes present in the cluster. If the request was sent to a free node, then this list will have exactly one entry. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_interfaces import ClusterInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInterfaces from a JSON string
cluster_interfaces_instance = ClusterInterfaces.from_json(json)
# print the JSON string representation of the object
print(ClusterInterfaces.to_json())

# convert the object into a dict
cluster_interfaces_dict = cluster_interfaces_instance.to_dict()
# create an instance of ClusterInterfaces from a dict
cluster_interfaces_from_dict = ClusterInterfaces.from_dict(cluster_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


