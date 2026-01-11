# FailoverReplicaCluster

Specifies the details about replication cluster involved in the failover operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[FailoverObject], none_type**](FailoverObject.md) | Specifies the details about the objects being failed over. In case if view based orchastrator is calling this then they should pass a object id for replicated view entity which belongs to the live tracking view on replication cluster. | 
**protection_group_id** | **str, none_type** | Specifies the protection group id from the replication cluster from where the objects being failed over. If this is not specified then it will be infer from the list of objects being failed over. The protection group id must be specified in this format &lt;cluster_id&gt;:&lt;cluster_incarnation_id:jobid&gt; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


