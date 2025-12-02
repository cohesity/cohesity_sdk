# PatchDataSourceConnectorRequest

Specifies the properties of a data-source connector to patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the connector. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.patch_data_source_connector_request import PatchDataSourceConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDataSourceConnectorRequest from a JSON string
patch_data_source_connector_request_instance = PatchDataSourceConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(PatchDataSourceConnectorRequest.to_json())

# convert the object into a dict
patch_data_source_connector_request_dict = patch_data_source_connector_request_instance.to_dict()
# create an instance of PatchDataSourceConnectorRequest from a dict
patch_data_source_connector_request_from_dict = PatchDataSourceConnectorRequest.from_dict(patch_data_source_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


