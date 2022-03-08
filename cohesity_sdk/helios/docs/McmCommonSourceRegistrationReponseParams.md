# McmCommonSourceRegistrationReponseParams

Specifies the parameters which are common between all Protection Source registrations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] [readonly] 
**region_id** | **str, none_type** | Specifies the region id. | [optional] [readonly] 
**id** | **str, none_type** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. | [optional] 
**name** | **str, none_type** | The user specified name for this source. | [optional] [readonly] 
**connections** | [**[ConnectionConfig], none_type**](ConnectionConfig.md) | Specifies the list of connections associated with this source. | [optional] 
**source_id** | **str, none_type** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


