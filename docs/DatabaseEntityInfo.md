# DatabaseEntityInfo

Object details about Oracle database entity info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_database_info** | [**ContainerDatabaseInfo**](ContainerDatabaseInfo.md) |  | [optional] 
**data_guard_info** | [**OracleDataGuardInfo**](OracleDataGuardInfo.md) |  | [optional] 
**db_type** | **str** | Specifies database type of oracle database. | [optional] 

## Example

```python
from cohesity_sdk.models.database_entity_info import DatabaseEntityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseEntityInfo from a JSON string
database_entity_info_instance = DatabaseEntityInfo.from_json(json)
# print the JSON string representation of the object
print(DatabaseEntityInfo.to_json())

# convert the object into a dict
database_entity_info_dict = database_entity_info_instance.to_dict()
# create an instance of DatabaseEntityInfo from a dict
database_entity_info_from_dict = DatabaseEntityInfo.from_dict(database_entity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


