# ClusterStatus

Describes the cluster status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airgap_config_stats** | [**AirgapConfig**](AirgapConfig.md) |  | [optional] 
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**current_operation** | **str** | Specifies the current operation of the cluster. | [optional] 
**message** | **str** | Specifies an optional message describing details of the cluster status. | [optional] 
**name** | **str** | Specifies the name of the cluster. | [optional] 
**node_statuses** | [**List[NodeStatusResult]**](NodeStatusResult.md) | Specifies the status of each node on the cluster. | [optional] 
**removal_state** | **str** | RemovalState specifies the possible states for removal operations happening on the cluster. | [optional] 
**services_synced** | **bool** | Specifies whether or not the services are synced with the list of stopped services. | [optional] 
**software_version** | **str** | Specifies the software version of the cluster. | [optional] 
**stopped_services** | **List[str]** | Specifies the service name. | [optional] 
**system_app_status** | [**List[SystemAppStatusParams]**](SystemAppStatusParams.md) | Specifies the status of each system app on the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_status import ClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatus from a JSON string
cluster_status_instance = ClusterStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterStatus.to_json())

# convert the object into a dict
cluster_status_dict = cluster_status_instance.to_dict()
# create an instance of ClusterStatus from a dict
cluster_status_from_dict = ClusterStatus.from_dict(cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


