# GlobalClusterIdentifier

Specifies the MCM cluster identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | [optional] 
**region_id** | **str** | Specifies the region id of the cluster. Only valid for DMaaS clusters. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.global_cluster_identifier import GlobalClusterIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalClusterIdentifier from a JSON string
global_cluster_identifier_instance = GlobalClusterIdentifier.from_json(json)
# print the JSON string representation of the object
print(GlobalClusterIdentifier.to_json())

# convert the object into a dict
global_cluster_identifier_dict = global_cluster_identifier_instance.to_dict()
# create an instance of GlobalClusterIdentifier from a dict
global_cluster_identifier_from_dict = GlobalClusterIdentifier.from_dict(global_cluster_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


