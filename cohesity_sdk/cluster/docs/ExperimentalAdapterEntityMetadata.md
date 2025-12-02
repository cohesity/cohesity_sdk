# ExperimentalAdapterEntityMetadata

Specifies the entity metadata of experimental adapter entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_metadata_params** | **str** | Specifies custom entity metadata for the experimental adapter entity. | [optional] 
**id** | **str** | Specifies the ID for the Experimental Adapter entity. | [optional] 
**password** | **str** | Specifies the password for the Experimental Adapter entity. | [optional] 
**username** | **str** | Specifies the username for the Experimental Adapter entity. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapter_entity_metadata import ExperimentalAdapterEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapterEntityMetadata from a JSON string
experimental_adapter_entity_metadata_instance = ExperimentalAdapterEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapterEntityMetadata.to_json())

# convert the object into a dict
experimental_adapter_entity_metadata_dict = experimental_adapter_entity_metadata_instance.to_dict()
# create an instance of ExperimentalAdapterEntityMetadata from a dict
experimental_adapter_entity_metadata_from_dict = ExperimentalAdapterEntityMetadata.from_dict(experimental_adapter_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


