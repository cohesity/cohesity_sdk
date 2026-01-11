# CommonSourceRegistrationReponseParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be deprecated in future. Use connections field. | [optional] 
**connections** | [**[ConnectionConfig], none_type**](ConnectionConfig.md) | Specifies the list of connections for the source. | [optional] 
**connector_group_id** | **int, none_type** | Specifies the connector group id of connector groups. | [optional] 
**data_source_connection_id** | **str, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. Also, this is the &#39;string&#39; of connectionId. This property was added to accommodate for ID values that exceed 2^53 - 1, which is the max value for which JS maintains precision. | [optional] 
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | [optional] 
**id** | **int, none_type** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**name** | **str, none_type** | The user specified name for this source. | [optional] 
**source_id** | **int, none_type** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**source_info** | [**Object**](Object.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


