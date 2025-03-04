# RemoteClusters

Specifies a list of Remote Cluster registered with the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_clusters** | [**List[UpdateRemoteClusterParams]**](UpdateRemoteClusterParams.md) | Specifies the list of Remote Clusters. | [optional] 

## Example

```python
from cohesity_sdk.models.remote_clusters import RemoteClusters

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteClusters from a JSON string
remote_clusters_instance = RemoteClusters.from_json(json)
# print the JSON string representation of the object
print(RemoteClusters.to_json())

# convert the object into a dict
remote_clusters_dict = remote_clusters_instance.to_dict()
# create an instance of RemoteClusters from a dict
remote_clusters_from_dict = RemoteClusters.from_dict(remote_clusters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


