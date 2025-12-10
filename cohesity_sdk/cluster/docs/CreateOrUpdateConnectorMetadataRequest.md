# CreateOrUpdateConnectorMetadataRequest

Specifies the request to create or update information about connector image files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_metadata** | [**ConnectorMetadata**](ConnectorMetadata.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.create_or_update_connector_metadata_request import CreateOrUpdateConnectorMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateConnectorMetadataRequest from a JSON string
create_or_update_connector_metadata_request_instance = CreateOrUpdateConnectorMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateConnectorMetadataRequest.to_json())

# convert the object into a dict
create_or_update_connector_metadata_request_dict = create_or_update_connector_metadata_request_instance.to_dict()
# create an instance of CreateOrUpdateConnectorMetadataRequest from a dict
create_or_update_connector_metadata_request_from_dict = CreateOrUpdateConnectorMetadataRequest.from_dict(create_or_update_connector_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


