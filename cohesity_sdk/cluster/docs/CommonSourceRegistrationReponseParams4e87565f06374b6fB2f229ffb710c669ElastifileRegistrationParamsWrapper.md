# CommonSourceRegistrationReponseParams4e87565f06374b6fB2f229ffb710c669ElastifileRegistrationParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**source_id** | **int, none_type** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**source_info** | [**Object**](Object.md) |  | [optional] 
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | [optional] 
**name** | **str, none_type** | The user specified name for this source. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be depricated in future. Use connections field. | [optional] 
**authentication_status** | **str, none_type** | Specifies the status of the authentication during the registration of a Protection Source. &#39;Pending&#39; indicates the authentication is in progress. &#39;Scheduled&#39; indicates the authentication is scheduled. &#39;Finished&#39; indicates the authentication is completed. &#39;RefreshInProgress&#39; indicates the refresh is in progress. | [optional] [readonly] 
**registration_time_msecs** | **int, none_type** | Specifies the time when the source was registered in milliseconds | [optional] [readonly] 
**last_refreshed_time_msecs** | **int, none_type** | Specifies the time when the source was last refreshed in milliseconds. | [optional] [readonly] 
**elastifile_params** | [**ElastifileRegistrationParams**](ElastifileRegistrationParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


