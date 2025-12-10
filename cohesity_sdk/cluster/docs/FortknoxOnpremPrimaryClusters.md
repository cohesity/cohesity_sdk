# FortknoxOnpremPrimaryClusters

Specifies a list of Fortknox Onprem Primary Clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fortknox_onprem_primary_clusters** | [**List[FortknoxOnpremPrimaryCluster]**](FortknoxOnpremPrimaryCluster.md) | Specifies the list of Fortknox Onprem Primary Clusters. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fortknox_onprem_primary_clusters import FortknoxOnpremPrimaryClusters

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxOnpremPrimaryClusters from a JSON string
fortknox_onprem_primary_clusters_instance = FortknoxOnpremPrimaryClusters.from_json(json)
# print the JSON string representation of the object
print(FortknoxOnpremPrimaryClusters.to_json())

# convert the object into a dict
fortknox_onprem_primary_clusters_dict = fortknox_onprem_primary_clusters_instance.to_dict()
# create an instance of FortknoxOnpremPrimaryClusters from a dict
fortknox_onprem_primary_clusters_from_dict = FortknoxOnpremPrimaryClusters.from_dict(fortknox_onprem_primary_clusters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


