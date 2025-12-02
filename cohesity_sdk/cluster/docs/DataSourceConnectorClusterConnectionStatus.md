# DataSourceConnectorClusterConnectionStatus

Specifies the data-source connector-cluster connectivity status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Specifies if the connection to the cluster is active. | [optional] 
**last_connected_timestamp_msecs** | **int** | Specifies last known connectivity status time in milliseconds. | [optional] 
**message** | **str** | Specifies possible connectivity error message. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_cluster_connection_status import DataSourceConnectorClusterConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorClusterConnectionStatus from a JSON string
data_source_connector_cluster_connection_status_instance = DataSourceConnectorClusterConnectionStatus.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorClusterConnectionStatus.to_json())

# convert the object into a dict
data_source_connector_cluster_connection_status_dict = data_source_connector_cluster_connection_status_instance.to_dict()
# create an instance of DataSourceConnectorClusterConnectionStatus from a dict
data_source_connector_cluster_connection_status_from_dict = DataSourceConnectorClusterConnectionStatus.from_dict(data_source_connector_cluster_connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


