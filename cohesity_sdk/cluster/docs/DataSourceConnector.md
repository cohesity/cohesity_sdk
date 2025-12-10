# DataSourceConnector

Specifies all the properties of the data-source connector. A connector is uniquely identified by a 'connectorId' for a given tenant. A connector resource is created internally by the system when a connector is registered with the cluster and thus, a POST API doesn't exist and isn't needed for creating a connector resource. An active connector is always associated with a data-source connection belonging to its tenant. A connector can never be associated with more than one connection/tenant/cluster at a given time. A connector also has a name which can be updated by the user. Names of connectors for a tenant or across tenants needn't be unique. Also, a connector constituent can optionally have two actively used NICs (dual-homed connectors).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_side_ip** | **str** | Specifies the IP of the connector&#39;s NIC facing the cluster. | [optional] [readonly] 
**connection_id** | **str** | Specifies the ID of the connection to which this connector belongs. | 
**connectivity_status** | [**ConnectorConnectivityStatus**](ConnectorConnectivityStatus.md) |  | [optional] 
**connector_id** | **str** | Specifies the unique ID of the connector. | 
**connector_name** | **str** | Specifies the name of the connector. The name of a connector need not be unique within a tenant or across tenants. The name of the connector can be updated as needed. | [optional] 
**patch_software_version** | **str** | Specifies the connector&#39;s patch software version. | [optional] [readonly] 
**patch_status** | [**ConnectorPatchStatus**](ConnectorPatchStatus.md) |  | [optional] 
**software_version** | **str** | Specifies the connector&#39;s software version. | [optional] [readonly] 
**tenant_side_ip** | **str** | Specifies the IP of the connector&#39;s NIC facing the sources of the tenant to which the connector belongs. | [optional] [readonly] 
**upgrade_status** | [**ConnectorUpgradeStatus**](ConnectorUpgradeStatus.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector import DataSourceConnector

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnector from a JSON string
data_source_connector_instance = DataSourceConnector.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnector.to_json())

# convert the object into a dict
data_source_connector_dict = data_source_connector_instance.to_dict()
# create an instance of DataSourceConnector from a dict
data_source_connector_from_dict = DataSourceConnector.from_dict(data_source_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


