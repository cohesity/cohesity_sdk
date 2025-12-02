# DataSourceConnector

Specifies all the properties of the data-source connector. A connector is uniquely identified by a 'connectorId' for a given tenant. A connector resource is created internally by the system when a connector is registered with the cluster and thus, a POST API doesn't exist and isn't needed for creating a connector resource. An active connector is always associated with a data-source connection belonging to its tenant. A connector can never be associated with more than one connection/tenant/cluster at a given time. A connector also has a name which can be updated by the user. Names of connectors for a tenant or across tenants needn't be unique. Also, a connector constituent can optionally have two actively used NICs (dual-homed connectors).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Specifies the ID of the connection to which this connector belongs. | 
**connector_id** | **str** | Specifies the unique ID of the connector. | 
**cluster_side_ip** | **str, none_type** | Specifies the IP of the connector&#39;s NIC facing the cluster. | [optional] [readonly] 
**connectivity_status** | [**ConnectorConnectivityStatus**](ConnectorConnectivityStatus.md) |  | [optional] 
**connector_name** | **str, none_type** | Specifies the name of the connector. The name of a connector need not be unique within a tenant or across tenants. The name of the connector can be updated as needed. | [optional] 
**patch_software_version** | **str, none_type** | Specifies the connector&#39;s patch software version. | [optional] [readonly] 
**patch_status** | [**ConnectorPatchStatus**](ConnectorPatchStatus.md) |  | [optional] 
**software_version** | **str, none_type** | Specifies the connector&#39;s software version. | [optional] [readonly] 
**tenant_side_ip** | **str, none_type** | Specifies the IP of the connector&#39;s NIC facing the sources of the tenant to which the connector belongs. | [optional] [readonly] 
**upgrade_status** | [**ConnectorUpgradeStatus**](ConnectorUpgradeStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


