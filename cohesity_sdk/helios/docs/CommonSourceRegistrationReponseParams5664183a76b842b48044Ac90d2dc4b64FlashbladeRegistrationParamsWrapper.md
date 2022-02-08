# CommonSourceRegistrationReponseParams5664183a76b842b48044Ac90d2dc4b64FlashbladeRegistrationParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**source_id** | **int, none_type** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**source_info** | [**Object**](Object.md) |  | [optional] 
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | [optional] 
**name** | **str, none_type** | The user specified name for this source. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**flashblade_params** | [**FlashbladeRegistrationParams**](FlashbladeRegistrationParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


