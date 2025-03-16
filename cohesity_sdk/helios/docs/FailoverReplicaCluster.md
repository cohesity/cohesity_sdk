# FailoverReplicaCluster

Specifies the details about replication cluster involved in the failover operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[FailoverObject]**](FailoverObject.md) | Specifies the details about the objects being failed over. In case if view based orchastrator is calling this then they should pass a object id for replicated view entity which belongs to the live tracking view on replication cluster. | 
**protection_group_id** | **str** | Specifies the protection group id from the replication cluster from where the objects being failed over. If this is not specified then it will be infer from the list of objects being failed over. The protection group id must be specified in this format &lt;cluster_id&gt;:&lt;cluster_incarnation_id:jobid&gt; | [optional] 

## Example

```python
from cohesity_sdk.helios.models.failover_replica_cluster import FailoverReplicaCluster

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverReplicaCluster from a JSON string
failover_replica_cluster_instance = FailoverReplicaCluster.from_json(json)
# print the JSON string representation of the object
print(FailoverReplicaCluster.to_json())

# convert the object into a dict
failover_replica_cluster_dict = failover_replica_cluster_instance.to_dict()
# create an instance of FailoverReplicaCluster from a dict
failover_replica_cluster_from_dict = FailoverReplicaCluster.from_dict(failover_replica_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


