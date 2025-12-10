# ConnectorImageFile

Specifies the URL to access the connector image file and the platform on which the image can be deployed. The software version of the connector is assumed to be derivable from the name of the image file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_type** | **str** | Specifies the platform on which the image can be deployed. | 
**url** | **str** | Specifies the URL to access the file. | 

## Example

```python
from cohesity_sdk.cluster.models.connector_image_file import ConnectorImageFile

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorImageFile from a JSON string
connector_image_file_instance = ConnectorImageFile.from_json(json)
# print the JSON string representation of the object
print(ConnectorImageFile.to_json())

# convert the object into a dict
connector_image_file_dict = connector_image_file_instance.to_dict()
# create an instance of ConnectorImageFile from a dict
connector_image_file_from_dict = ConnectorImageFile.from_dict(connector_image_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


