# SQLServerInstance

Specifies the details of a SQL server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[ResourceEndpoint]**](ResourceEndpoint.md) | Specifies the information about endpoint associated with this SQL server instance. | [optional] 
**id** | **str** | Specifies the unique id of the SQL server instance. | [optional] 
**is_online** | **str** | Specifies the wehther the SQL server instance is online or not. | [optional] 
**is_partof_fci** | **bool** | Specifies whether this SQL server instance is a part of Failover cluster or not. | [optional] 
**name** | **str** | Specifies the name of the SQL server instance. | [optional] 

## Example

```python
from cohesity_sdk.models.sql_server_instance import SQLServerInstance

# TODO update the JSON string below
json = "{}"
# create an instance of SQLServerInstance from a JSON string
sql_server_instance_instance = SQLServerInstance.from_json(json)
# print the JSON string representation of the object
print(SQLServerInstance.to_json())

# convert the object into a dict
sql_server_instance_dict = sql_server_instance_instance.to_dict()
# create an instance of SQLServerInstance from a dict
sql_server_instance_from_dict = SQLServerInstance.from_dict(sql_server_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


