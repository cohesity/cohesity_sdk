# DataSourceConnectorLocalStatus

Specifies the data-source connector status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_connection_status** | [**DataSourceConnectorClusterConnectionStatus**](DataSourceConnectorClusterConnectionStatus.md) |  | [optional] 
**is_certificate_valid** | **bool** | Flag to indicate if connector certificate is valid. | [optional] 
**registration_status** | [**DataSourceConnectorRegistrationStatus**](DataSourceConnectorRegistrationStatus.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_local_status import DataSourceConnectorLocalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorLocalStatus from a JSON string
data_source_connector_local_status_instance = DataSourceConnectorLocalStatus.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorLocalStatus.to_json())

# convert the object into a dict
data_source_connector_local_status_dict = data_source_connector_local_status_instance.to_dict()
# create an instance of DataSourceConnectorLocalStatus from a dict
data_source_connector_local_status_from_dict = DataSourceConnectorLocalStatus.from_dict(data_source_connector_local_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


