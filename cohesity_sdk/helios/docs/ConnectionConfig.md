# ConnectionConfig

Specifies a connection associated with the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** | Specifies the id of the connection. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**entity_id** | **int** | Specifies the entity id of the source. The source can a non-root entity. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.connection_config import ConnectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConfig from a JSON string
connection_config_instance = ConnectionConfig.from_json(json)
# print the JSON string representation of the object
print(ConnectionConfig.to_json())

# convert the object into a dict
connection_config_dict = connection_config_instance.to_dict()
# create an instance of ConnectionConfig from a dict
connection_config_from_dict = ConnectionConfig.from_dict(connection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


