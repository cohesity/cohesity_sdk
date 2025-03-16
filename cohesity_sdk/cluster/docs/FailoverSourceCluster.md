# FailoverSourceCluster

Specifies the details about source cluster involved in the failover operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the source cluster Id involved in failover operation. | 
**incarnation_id** | **int** | Specifies the source cluster incarnation Id involved in failover operation. | [optional] [readonly] 
**protection_group_id** | **str** | Specifies the protection group Id involved in failover operation. | [optional] [readonly] 
**view_id** | **int** | If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.failover_source_cluster import FailoverSourceCluster

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverSourceCluster from a JSON string
failover_source_cluster_instance = FailoverSourceCluster.from_json(json)
# print the JSON string representation of the object
print(FailoverSourceCluster.to_json())

# convert the object into a dict
failover_source_cluster_dict = failover_source_cluster_instance.to_dict()
# create an instance of FailoverSourceCluster from a dict
failover_source_cluster_from_dict = FailoverSourceCluster.from_dict(failover_source_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


