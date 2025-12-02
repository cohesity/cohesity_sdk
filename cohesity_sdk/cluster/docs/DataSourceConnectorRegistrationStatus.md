# DataSourceConnectorRegistrationStatus

Specifies the data-source connector registration status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the message corresponding the registration. | [optional] 
**status** | **str** | Specifies the registration status. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_registration_status import DataSourceConnectorRegistrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorRegistrationStatus from a JSON string
data_source_connector_registration_status_instance = DataSourceConnectorRegistrationStatus.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorRegistrationStatus.to_json())

# convert the object into a dict
data_source_connector_registration_status_dict = data_source_connector_registration_status_instance.to_dict()
# create an instance of DataSourceConnectorRegistrationStatus from a dict
data_source_connector_registration_status_from_dict = DataSourceConnectorRegistrationStatus.from_dict(data_source_connector_registration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


