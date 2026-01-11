# ClusterStatus

Describes the cluster status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airgap_config_stats** | [**AirgapConfig**](AirgapConfig.md) |  | [optional] 
**cluster_id** | **int, none_type** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] 
**current_operation** | **str, none_type** | Specifies the current operation of the cluster. | [optional] 
**message** | **str, none_type** | Specifies an optional message describing details of the cluster status. | [optional] 
**name** | **str, none_type** | Specifies the name of the cluster. | [optional] 
**node_statuses** | [**[NodeStatusResult], none_type**](NodeStatusResult.md) | Specifies the status of each node on the cluster. | [optional] 
**removal_state** | **str, none_type** | RemovalState specifies the possible states for removal operations happening on the cluster. | [optional] 
**services_synced** | **bool, none_type** | Specifies whether or not the services are synced with the list of stopped services. | [optional] 
**software_version** | **str, none_type** | Specifies the software version of the cluster. | [optional] 
**stopped_services** | **[str], none_type** | Specifies the service name. | [optional] 
**system_app_status** | [**[SystemAppStatusParams], none_type**](SystemAppStatusParams.md) | Specifies the status of each system app on the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


