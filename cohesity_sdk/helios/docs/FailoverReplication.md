# FailoverReplication

Specifies the details of a failover replication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the replication complete time in micro seconds. | [optional] 
**error_message** | **str** | Specifies the error details if replication status is &#39;Failed&#39;. | [optional] 
**id** | **str** | Specifies the replication id. | [optional] 
**logical_bytes_transferred** | **int** | Specifies the number of logical bytes transferred for this replication so far. This value can never exceed the total logical size of the replicated view. | [optional] 
**logical_size_bytes** | **int** | Specifies the total amount of logical data to be transferred for this replication. | [optional] 
**percentage_completed** | **int** | Specifies the percentage completed in the replication. | [optional] 
**physical_bytes_transferred** | **int** | Specifies the number of bytes sent over the wire for this replication so far. | [optional] 
**start_time_usecs** | **int** | Specifies the replication start time in micro seconds. | [optional] 
**status** | **str** | Specifies the replication status. | [optional] 
**target_cluster_id** | **int** | Specifies the failover target cluster id. | [optional] 
**target_cluster_incarnation_id** | **int** | Specifies the failover target cluster incarnation id. | [optional] 
**target_cluster_name** | **str** | Specifies the failover target cluster name. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.failover_replication import FailoverReplication

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverReplication from a JSON string
failover_replication_instance = FailoverReplication.from_json(json)
# print the JSON string representation of the object
print(FailoverReplication.to_json())

# convert the object into a dict
failover_replication_dict = failover_replication_instance.to_dict()
# create an instance of FailoverReplication from a dict
failover_replication_from_dict = FailoverReplication.from_dict(failover_replication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


