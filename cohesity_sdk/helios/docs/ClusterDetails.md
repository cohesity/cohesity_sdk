# ClusterDetails

Specifies the array of clusters details including internally and externally claimed clusters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohesity_clusters** | [**List[ClusterInfo]**](ClusterInfo.md) | Specifies the array of clusters upgrade details | [optional] 
**sp_clusters** | [**List[SPClusterInfo]**](SPClusterInfo.md) | Specifies the array of clusters claimed from IBM Storage Protect environment. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_details import ClusterDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDetails from a JSON string
cluster_details_instance = ClusterDetails.from_json(json)
# print the JSON string representation of the object
print(ClusterDetails.to_json())

# convert the object into a dict
cluster_details_dict = cluster_details_instance.to_dict()
# create an instance of ClusterDetails from a dict
cluster_details_from_dict = ClusterDetails.from_dict(cluster_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


