# ReplicationBackupActivationResult

Specifies the result returned after creating a protection group for backing up failover objects on replication cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_errors** | [**List[Error]**](Error.md) | Specifies the protection errors, if any, pertaining to each object specified in &#39;objects&#39;. | [optional] 
**objects** | [**List[FailoverObject]**](FailoverObject.md) | Specifies the list of failover object that are going to be protected on replication cluster. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id that will be returned upon creation of new group or existing group for backing up failover entities. | [optional] 
**reverse_replication_result** | [**ReverseReplicationResult**](ReverseReplicationResult.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.replication_backup_activation_result import ReplicationBackupActivationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationBackupActivationResult from a JSON string
replication_backup_activation_result_instance = ReplicationBackupActivationResult.from_json(json)
# print the JSON string representation of the object
print(ReplicationBackupActivationResult.to_json())

# convert the object into a dict
replication_backup_activation_result_dict = replication_backup_activation_result_instance.to_dict()
# create an instance of ReplicationBackupActivationResult from a dict
replication_backup_activation_result_from_dict = ReplicationBackupActivationResult.from_dict(replication_backup_activation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


