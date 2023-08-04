# NodeEndpointState

Specify the results after checking connectivity on endpoints on each node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the Id of the node. | [optional] 
**endpoints** | [**[EndpointConnectionState], none_type**](EndpointConnectionState.md) | Specifies the results of the endpoints. | [optional] 
**gateway_reachability** | [**EndpointConnectionState**](EndpointConnectionState.md) |  | [optional] 
**dns_server_reachability** | [**EndpointConnectionState**](EndpointConnectionState.md) |  | [optional] 
**ntp_server_reachability** | [**EndpointConnectionState**](EndpointConnectionState.md) |  | [optional] 
**check_timestamp_usecs** | **int, none_type** | Specifies the time in Epoch in micro seconds when the check is performed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


