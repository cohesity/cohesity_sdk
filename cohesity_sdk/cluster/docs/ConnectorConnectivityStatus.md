# ConnectorConnectivityStatus

Specifies connectvity status information for the data-source connector. For example if it's currently connected to the cluster, when it last connected to the cluster successfully, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_connected** | **bool** | Specifies whether the connector is currently connected to the cluster. | 
**connected_since_timestamp_secs** | **int, none_type** | This denotes the timestamp in UNIX seconds since which this connector has been connected to its cluster without any interruptions. This property will NOT be present if this connector is not currently connected to its cluster. | [optional] 
**last_connected_timestamp_secs** | **int, none_type** | Same as the property &#39;connectedSinceTimestampSecs&#39;. This is deprecated and will be removed eventually. Use &#39;connectedSinceTimestampSecs&#39; instead. | [optional] 
**last_known_health_ok_timestamp_secs** | **int, none_type** | Specifies the most recent known timestamp in UNIX seconds at which this connector passed the health checks. This property can be present even if this connector is not currently connected to its cluster. | [optional] 
**message** | **str, none_type** | Specifies error message when the connector is unable to connect to the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


