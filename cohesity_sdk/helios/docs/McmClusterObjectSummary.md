# McmClusterObjectSummary

Specifies the objects summary for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the ID of the cluster to which the source is registered. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**summary** | [**List[McmObjectSummary]**](McmObjectSummary.md) | Specifies the object summary. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_cluster_object_summary import McmClusterObjectSummary

# TODO update the JSON string below
json = "{}"
# create an instance of McmClusterObjectSummary from a JSON string
mcm_cluster_object_summary_instance = McmClusterObjectSummary.from_json(json)
# print the JSON string representation of the object
print(McmClusterObjectSummary.to_json())

# convert the object into a dict
mcm_cluster_object_summary_dict = mcm_cluster_object_summary_instance.to_dict()
# create an instance of McmClusterObjectSummary from a dict
mcm_cluster_object_summary_from_dict = McmClusterObjectSummary.from_dict(mcm_cluster_object_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


