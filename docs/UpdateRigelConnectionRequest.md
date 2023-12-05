# UpdateRigelConnectionRequest

Specify the params to update a connection of Rigel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the connection. | 
**tenant_id** | **str, none_type** | Specifies the id of the tenant which the connection belongs to. | 
**scalable** | **bool, none_type** | Flag to specify if the connection is scalable. | [optional] 
**connector_groups** | [**[ConnectorGroup]**](ConnectorGroup.md) | Specifies the connector groups in the connection. | [optional] 
**ungrouped_connectors** | **[int]** | Specifies the ids of the connectors which are not grouped in this connection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


