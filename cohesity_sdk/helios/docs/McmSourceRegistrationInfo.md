# McmSourceRegistrationInfo

Specifies the registration details and errors occured during registration of a protection source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. | [optional] 
**connections** | [**[ConnectionConfig], none_type**](ConnectionConfig.md) | Specifies the list of connections associated with this source. | [optional] 
**registration_time_usecs** | **int, none_type** | Specifies the registration time of the Source in Unix time epoch in microseconds. | [optional] 
**registration_error** | **str, none_type** | Specifies the error detail occured during the protection source registration. | [optional] 
**last_refresh_time_usecs** | **int, none_type** | Specifies the registration time of the Source in Unix time epoch in microseconds. | [optional] 
**refresh_error** | **str, none_type** | Specifies the error detail occured during the refersh of a protection source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


