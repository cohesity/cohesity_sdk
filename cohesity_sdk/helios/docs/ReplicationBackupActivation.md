# ReplicationBackupActivation

Specifies the request parmeters to activate the backup of failover entities on replication cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_object_backup** | **bool** | If set to true then object based backups will be created for the failed over VMs. | [optional] 
**do_not_protect** | **bool** | Whether to skip protecting the failed over entities previously specified via Initiate Failover API. | [optional] 
**enable_reverse_replication** | **bool** | If this is specifed as true, then reverse replication of failover objects will be enabled from replication cluster to source cluster. If source cluster is not reachable, then replications will fail until source cluster comes up again. Here orchastrator should also ensure that storage domain on replication cluster is correctly mapped to the same storage domain on the source cluster. | [optional] 
**objects** | [**List[FailoverObject]**](FailoverObject.md) | Specifies the list of failover object that need to be protected on replication cluster. If the object set that was sent earlier is provided again then API will return an error. If this objects list is not specified then internally it will be inferred if &#39;/objectLinkage&#39; API has been called previously. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id that will be used for backing up the failover entities on replication cluster. This is a optional argument and only need to be passed if user wants to use the existing job for the backup. If specified then Orchastrator should enusre that protection group is compatible to handle all provided failover objects. | [optional] 
**target_failover_environment** | **str** | If this is specified, then the protection environment of the failed over objects will be set to this. Otherwise, the protection environment of the failed over objects is determined by the objects&#39; environment. | [optional] 
**target_failover_policy_id** | **str** | Policy which will be used in the protection of the failed over objects. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.replication_backup_activation import ReplicationBackupActivation

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationBackupActivation from a JSON string
replication_backup_activation_instance = ReplicationBackupActivation.from_json(json)
# print the JSON string representation of the object
print(ReplicationBackupActivation.to_json())

# convert the object into a dict
replication_backup_activation_dict = replication_backup_activation_instance.to_dict()
# create an instance of ReplicationBackupActivation from a dict
replication_backup_activation_from_dict = ReplicationBackupActivation.from_dict(replication_backup_activation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


