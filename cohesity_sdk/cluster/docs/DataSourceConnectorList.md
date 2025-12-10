# DataSourceConnectorList

Specifies a list of data-source connectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectors** | [**List[DataSourceConnector]**](DataSourceConnector.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_list import DataSourceConnectorList

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorList from a JSON string
data_source_connector_list_instance = DataSourceConnectorList.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorList.to_json())

# convert the object into a dict
data_source_connector_list_dict = data_source_connector_list_instance.to_dict()
# create an instance of DataSourceConnectorList from a dict
data_source_connector_list_from_dict = DataSourceConnectorList.from_dict(data_source_connector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


