# ConnectionConnectivityStatus

Specifies connectivity status information for the data-source connection. It represents information such as, if there's at least one active connector, latest time at which any connector(s) in this connection passed health checks, since how long there has been at least one active connector, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_since_timestamp_secs** | **int** | This denotes the timestamp in UNIX seconds since which this connection has at least one connector connected to the cluster without any interruptions. This property will NOT be present if none of the connectors in this connection are currently connected to the cluster. | [optional] 
**is_connected** | **bool** | Specifies whether the connection has any of its connectors connected. | 
**last_known_health_ok_timestamp_secs** | **int** | Specifies the most recent known timestamp in UNIX seconds at which any connector(s) in this connection passed the health checks. This property can be present even if no connectors in this connection are currently connected to the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connection_connectivity_status import ConnectionConnectivityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConnectivityStatus from a JSON string
connection_connectivity_status_instance = ConnectionConnectivityStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectionConnectivityStatus.to_json())

# convert the object into a dict
connection_connectivity_status_dict = connection_connectivity_status_instance.to_dict()
# create an instance of ConnectionConnectivityStatus from a dict
connection_connectivity_status_from_dict = ConnectionConnectivityStatus.from_dict(connection_connectivity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


