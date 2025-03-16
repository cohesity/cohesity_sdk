# McmClusterIdentifier

Specifies the MCM cluster identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**region_id** | **str** | Specifies the region id of the cluster. Only valid for DMaaS clusters. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_cluster_identifier import McmClusterIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of McmClusterIdentifier from a JSON string
mcm_cluster_identifier_instance = McmClusterIdentifier.from_json(json)
# print the JSON string representation of the object
print(McmClusterIdentifier.to_json())

# convert the object into a dict
mcm_cluster_identifier_dict = mcm_cluster_identifier_instance.to_dict()
# create an instance of McmClusterIdentifier from a dict
mcm_cluster_identifier_from_dict = McmClusterIdentifier.from_dict(mcm_cluster_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


