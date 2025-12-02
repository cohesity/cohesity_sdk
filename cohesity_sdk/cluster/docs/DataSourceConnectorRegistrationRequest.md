# DataSourceConnectorRegistrationRequest

Specifies the request to register a data-source connector. The registration token for the data-source connection with which this connector is to be registered has to be obtained by the user by invoking the relevant '/data-source-connections' APIs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_token** | **str** | The registration token. | 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connector_registration_request import DataSourceConnectorRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnectorRegistrationRequest from a JSON string
data_source_connector_registration_request_instance = DataSourceConnectorRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnectorRegistrationRequest.to_json())

# convert the object into a dict
data_source_connector_registration_request_dict = data_source_connector_registration_request_instance.to_dict()
# create an instance of DataSourceConnectorRegistrationRequest from a dict
data_source_connector_registration_request_from_dict = DataSourceConnectorRegistrationRequest.from_dict(data_source_connector_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


