# CommonSourceRegistrationRequestParams87a8b0b01c2c4381B6c93209126747bePhysicalSourceRegistrationParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | 
**name** | **str, none_type** | A user specified name for this source. | [optional] 
**is_internal_encrypted** | **bool, none_type** | Specifies if credentials are encrypted by internal key. | [optional] 
**encryption_key** | **str, none_type** | Specifies the key that user has encrypted the credential with. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**physical_params** | [**PhysicalSourceRegistrationParams**](PhysicalSourceRegistrationParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


