# FailoverRunConfiguration

Specifies the configuration required for execting special run as a part of failover workflow. This special run is triggered during palnned failover to sync the source cluster to replication cluster with minimum possible delta. Please note that if this object is passed then this special run will ignore the other archivals and retention settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_non_failover_runs** | **bool** | If set to true, other ongoing runs backing up the same set of entities being failed over will be initiated for cancellation. Non conflicting run operations such as replications to other clusters, archivals will not be cancelled. If set to false, then new run will wait for all the pending operations to finish normally before scheduling a new backup/replication. | [optional] 
**objects** | [**List[FailoverObject]**](FailoverObject.md) | Specifies the list of all local entity ids of all the objects being failed from the source cluster. | 
**pause_next_runs** | **bool** | If this is set to true then unless failover operation is completed, all the next runs will be pasued. | [optional] 
**protection_group_id** | **str** | Specifies the active protection group id on the source cluster from where the objects are being failed over. | [optional] 
**replication_cluster_id** | **int** | Specifies the replication cluster Id where planned run will replicate objects. | 
**run_type** | **str** | Specifies the type of the backup run to be triggered by this request. If this is not set defaults to incremental backup. | [optional] 
**view_id** | **int** | If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.failover_run_configuration import FailoverRunConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverRunConfiguration from a JSON string
failover_run_configuration_instance = FailoverRunConfiguration.from_json(json)
# print the JSON string representation of the object
print(FailoverRunConfiguration.to_json())

# convert the object into a dict
failover_run_configuration_dict = failover_run_configuration_instance.to_dict()
# create an instance of FailoverRunConfiguration from a dict
failover_run_configuration_from_dict = FailoverRunConfiguration.from_dict(failover_run_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


