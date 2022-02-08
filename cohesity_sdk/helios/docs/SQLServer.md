# SQLServer

Specifies the details of a SQL server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique identifier of the SQL server host. | [optional] 
**resource_info** | [**AppResource**](AppResource.md) |  | [optional] 
**agent_info** | [**AgentInformation**](AgentInformation.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**is_primary** | **bool, none_type** | Indicates whether this is a active node of a FCI cluster or hosts primary replica of a AAG group. | [optional] 
**instances** | [**[SQLServerInstance], none_type**](SQLServerInstance.md) | Specifies the list of all sql instances running inside the current SQL host. | [optional] 
**is_selected_by_default** | **bool, none_type** | Indicates to the UI whether this server should be selected by default | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


