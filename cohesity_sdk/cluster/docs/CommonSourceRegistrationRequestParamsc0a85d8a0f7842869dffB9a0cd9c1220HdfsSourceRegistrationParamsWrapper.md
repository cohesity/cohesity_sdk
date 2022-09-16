# CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220HdfsSourceRegistrationParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | 
**name** | **str, none_type** | A user specified name for this source. | [optional] 
**is_internal_encrypted** | **bool, none_type** | Specifies if credentials are encrypted by internal key. | [optional] 
**encryption_key** | **str, none_type** | Specifies the key that user has encrypted the credential with. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**hdfs_params** | [**HdfsSourceRegistrationParams**](HdfsSourceRegistrationParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


