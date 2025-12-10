# ConnectorImageMetadata

Specifies information about the connector images for various platforms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_image_file_list** | [**List[ConnectorImageFile]**](ConnectorImageFile.md) | Specifies info about connector images for the supported platforms. | 

## Example

```python
from cohesity_sdk.cluster.models.connector_image_metadata import ConnectorImageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorImageMetadata from a JSON string
connector_image_metadata_instance = ConnectorImageMetadata.from_json(json)
# print the JSON string representation of the object
print(ConnectorImageMetadata.to_json())

# convert the object into a dict
connector_image_metadata_dict = connector_image_metadata_instance.to_dict()
# create an instance of ConnectorImageMetadata from a dict
connector_image_metadata_from_dict = ConnectorImageMetadata.from_dict(connector_image_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


