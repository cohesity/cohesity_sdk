# ReplicationBackupActivation

Specifies the request parmeters to activate the backup of failover entities on replication cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_object_backup** | **bool, none_type** | If set to true then object based backups will be created for the failed over VMs. | [optional] 
**do_not_protect** | **bool, none_type** | Whether to skip protecting the failed over entities previously specified via Initiate Failover API. | [optional] 
**enable_reverse_replication** | **bool, none_type** | If this is specifed as true, then reverse replication of failover objects will be enabled from replication cluster to source cluster. If source cluster is not reachable, then replications will fail until source cluster comes up again. Here orchastrator should also ensure that storage domain on replication cluster is correctly mapped to the same storage domain on the source cluster. | [optional] 
**objects** | [**[FailoverObject], none_type**](FailoverObject.md) | Specifies the list of failover object that need to be protected on replication cluster. If the object set that was sent earlier is provided again then API will return an error. If this objects list is not specified then internally it will be inferred if &#39;/objectLinkage&#39; API has been called previously. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id that will be used for backing up the failover entities on replication cluster. This is a optional argument and only need to be passed if user wants to use the existing job for the backup. If specified then Orchastrator should enusre that protection group is compatible to handle all provided failover objects. | [optional] 
**target_failover_environment** | **str, none_type** | If this is specified, then the protection environment of the failed over objects will be set to this. Otherwise, the protection environment of the failed over objects is determined by the objects&#39; environment. | [optional] 
**target_failover_policy_id** | **str, none_type** | Policy which will be used in the protection of the failed over objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


