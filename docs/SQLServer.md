# SQLServer

Specifies the details of a SQL server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_info** | [**AgentInformation**](AgentInformation.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**id** | **str** | Specifies the unique identifier of the SQL server host. | [optional] 
**instances** | [**List[SQLServerInstance]**](SQLServerInstance.md) | Specifies the list of all sql instances running inside the current SQL host. | [optional] 
**is_primary** | **bool** | Indicates whether this is a active node of a FCI cluster or hosts primary replica of a AAG group. | [optional] 
**is_selected_by_default** | **bool** | Indicates to the UI whether this server should be selected by default | [optional] 
**resource_info** | [**AppResource**](AppResource.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.sql_server import SQLServer

# TODO update the JSON string below
json = "{}"
# create an instance of SQLServer from a JSON string
sql_server_instance = SQLServer.from_json(json)
# print the JSON string representation of the object
print(SQLServer.to_json())

# convert the object into a dict
sql_server_dict = sql_server_instance.to_dict()
# create an instance of SQLServer from a dict
sql_server_from_dict = SQLServer.from_dict(sql_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


