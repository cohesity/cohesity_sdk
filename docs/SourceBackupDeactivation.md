# SourceBackupDeactivation

Specifies the request parmeters to deactivate the backup of failover entities on source cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keep_failover_objects** | **bool** | If this is set to true then objects will not be removed from protection group. If this is set to false, then all objects which are being failed over will be removed from the protection group. If protection group left with zero entities then it will be paused automatically. | [optional] 
**objects** | [**List[FailoverObject]**](FailoverObject.md) | Specifies the list of all local entity ids of all the objects being failed from the source cluster. Backup will be deactiaved for all given objects. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id of the source cluster from where the objects being failed over. If this is not specified then it will be infer from the list of objects being failed over. | [optional] 
**replication_cluster_id** | **int** | Specifies the replication cluster Id involved in failover operation. | [optional] 
**view_id** | **str** | If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over. Backup will be deactivated for view object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.source_backup_deactivation import SourceBackupDeactivation

# TODO update the JSON string below
json = "{}"
# create an instance of SourceBackupDeactivation from a JSON string
source_backup_deactivation_instance = SourceBackupDeactivation.from_json(json)
# print the JSON string representation of the object
print(SourceBackupDeactivation.to_json())

# convert the object into a dict
source_backup_deactivation_dict = source_backup_deactivation_instance.to_dict()
# create an instance of SourceBackupDeactivation from a dict
source_backup_deactivation_from_dict = SourceBackupDeactivation.from_dict(source_backup_deactivation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


