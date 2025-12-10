# DataSourceConnectorLogs

Specifies the data-source connector logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_logs** | [**List[DataSourceConnectorLog]**](DataSourceConnectorLog.md) | Specifies the data-source connector logs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_logs import DataSourceConnectorLogs

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorLogs from a JSON string
data_source_connector_logs_instance = DataSourceConnectorLogs.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorLogs.to_json())

# convert the object into a dict
data_source_connector_logs_dict = data_source_connector_logs_instance.to_dict()
# create an instance of DataSourceConnectorLogs from a dict
data_source_connector_logs_from_dict = DataSourceConnectorLogs.from_dict(data_source_connector_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


