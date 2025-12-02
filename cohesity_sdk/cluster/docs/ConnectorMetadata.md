# ConnectorMetadata

Specifies information about the connector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_image_metadata** | [**ConnectorImageMetadata**](ConnectorImageMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connector_metadata import ConnectorMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorMetadata from a JSON string
connector_metadata_instance = ConnectorMetadata.from_json(json)
# print the JSON string representation of the object
print(ConnectorMetadata.to_json())

# convert the object into a dict
connector_metadata_dict = connector_metadata_instance.to_dict()
# create an instance of ConnectorMetadata from a dict
connector_metadata_from_dict = ConnectorMetadata.from_dict(connector_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


