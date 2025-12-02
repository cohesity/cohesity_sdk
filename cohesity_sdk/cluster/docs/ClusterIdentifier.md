# ClusterIdentifier

Specifies the information about a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str** | Specifies the name of the cluster. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_identifier import ClusterIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterIdentifier from a JSON string
cluster_identifier_instance = ClusterIdentifier.from_json(json)
# print the JSON string representation of the object
print(ClusterIdentifier.to_json())

# convert the object into a dict
cluster_identifier_dict = cluster_identifier_instance.to_dict()
# create an instance of ClusterIdentifier from a dict
cluster_identifier_from_dict = ClusterIdentifier.from_dict(cluster_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


