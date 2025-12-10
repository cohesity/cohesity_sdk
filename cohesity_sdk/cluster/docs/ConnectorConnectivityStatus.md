# ConnectorConnectivityStatus

Specifies connectvity status information for the data-source connector. For example if it's currently connected to the cluster, when it last connected to the cluster successfully, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_since_timestamp_secs** | **int** | This denotes the timestamp in UNIX seconds since which this connector has been connected to its cluster without any interruptions. This property will NOT be present if this connector is not currently connected to its cluster. | [optional] 
**is_connected** | **bool** | Specifies whether the connector is currently connected to the cluster. | 
**last_connected_timestamp_secs** | **int** | Same as the property &#39;connectedSinceTimestampSecs&#39;. This is deprecated and will be removed eventually. Use &#39;connectedSinceTimestampSecs&#39; instead. | [optional] 
**last_known_health_ok_timestamp_secs** | **int** | Specifies the most recent known timestamp in UNIX seconds at which this connector passed the health checks. This property can be present even if this connector is not currently connected to its cluster. | [optional] 
**message** | **str** | Specifies error message when the connector is unable to connect to the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connector_connectivity_status import ConnectorConnectivityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorConnectivityStatus from a JSON string
connector_connectivity_status_instance = ConnectorConnectivityStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorConnectivityStatus.to_json())

# convert the object into a dict
connector_connectivity_status_dict = connector_connectivity_status_instance.to_dict()
# create an instance of ConnectorConnectivityStatus from a dict
connector_connectivity_status_from_dict = ConnectorConnectivityStatus.from_dict(connector_connectivity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


