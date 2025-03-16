# ContainerDatabaseInfo

Object details about Oracle container database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pluggable_database_list** | [**List[PluggableDatabaseInfo]**](PluggableDatabaseInfo.md) | Specifies the list of Pluggable databases within a container database. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.container_database_info import ContainerDatabaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerDatabaseInfo from a JSON string
container_database_info_instance = ContainerDatabaseInfo.from_json(json)
# print the JSON string representation of the object
print(ContainerDatabaseInfo.to_json())

# convert the object into a dict
container_database_info_dict = container_database_info_instance.to_dict()
# create an instance of ContainerDatabaseInfo from a dict
container_database_info_from_dict = ContainerDatabaseInfo.from_dict(container_database_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


