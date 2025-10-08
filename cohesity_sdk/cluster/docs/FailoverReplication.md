# FailoverReplication

Specifies the details of a failover replication.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int, none_type** | Specifies the replication complete time in micro seconds. | [optional] 
**error_message** | **str, none_type** | Specifies the error details if replication status is &#39;Failed&#39;. | [optional] 
**id** | **str, none_type** | Specifies the replication id. | [optional] 
**logical_bytes_transferred** | **int, none_type** | Specifies the number of logical bytes transferred for this replication so far. This value can never exceed the total logical size of the replicated view. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies the total amount of logical data to be transferred for this replication. | [optional] 
**percentage_completed** | **int, none_type** | Specifies the percentage completed in the replication. | [optional] 
**physical_bytes_transferred** | **int, none_type** | Specifies the number of bytes sent over the wire for this replication so far. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the replication start time in micro seconds. | [optional] 
**status** | **str, none_type** | Specifies the replication status. | [optional] 
**target_cluster_id** | **int, none_type** | Specifies the failover target cluster id. | [optional] 
**target_cluster_incarnation_id** | **int, none_type** | Specifies the failover target cluster incarnation id. | [optional] 
**target_cluster_name** | **str, none_type** | Specifies the failover target cluster name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


