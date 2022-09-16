# ReplicationBackupActivationResult

Specifies the result returned after creating a protection group for backing up failover objects on replication cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_id** | **str, none_type** | Specifies the protection group id that will be returned upon creation of new group or existing group for backing up failover entities. | [optional] 
**reverse_replication_result** | [**ReverseReplicationResult**](ReverseReplicationResult.md) |  | [optional] 
**objects** | [**[FailoverObject], none_type**](FailoverObject.md) | Specifies the list of failover object that are going to be protected on replication cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


