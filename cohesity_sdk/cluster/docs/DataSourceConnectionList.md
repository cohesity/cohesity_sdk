# DataSourceConnectionList

Specifies a list of data-source connections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[DataSourceConnection]**](DataSourceConnection.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connection_list import DataSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectionList from a JSON string
data_source_connection_list_instance = DataSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectionList.to_json())

# convert the object into a dict
data_source_connection_list_dict = data_source_connection_list_instance.to_dict()
# create an instance of DataSourceConnectionList from a dict
data_source_connection_list_from_dict = DataSourceConnectionList.from_dict(data_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


