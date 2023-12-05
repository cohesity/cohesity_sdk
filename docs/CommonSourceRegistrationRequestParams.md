# CommonSourceRegistrationRequestParams

Specifies the parameters which are common between all Protection Source registrations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**connections** | [**[ConnectionConfig], none_type**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int, none_type** | Specifies the connector group id of connector groups. | [optional] 
**encryption_key** | **str, none_type** | Specifies the key that user has encrypted the credential with. | [optional] 
**is_internal_encrypted** | **bool, none_type** | Specifies if credentials are encrypted by internal key. | [optional] 
**name** | **str, none_type** | A user specified name for this source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


