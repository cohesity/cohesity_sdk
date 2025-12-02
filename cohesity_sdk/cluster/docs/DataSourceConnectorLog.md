# DataSourceConnectorLog

Specifies a connector event log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the message of this event. | [optional] 
**timestamp_msecs** | **int** | Specifies the time stamp in milliseconds of the event. | [optional] 
**type** | **str** | Specifies the severity of the event. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_log import DataSourceConnectorLog

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorLog from a JSON string
data_source_connector_log_instance = DataSourceConnectorLog.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorLog.to_json())

# convert the object into a dict
data_source_connector_log_dict = data_source_connector_log_instance.to_dict()
# create an instance of DataSourceConnectorLog from a dict
data_source_connector_log_from_dict = DataSourceConnectorLog.from_dict(data_source_connector_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


