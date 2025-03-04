# AssociateEntityMetadataResultParams

Specifies the response parameters for the AssociateEntityMetadataRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Specifies the entity id of the object. | [optional] 
**error_message** | **str** | Specifies an error message (if any) corresponding to this entityId. | [optional] 
**error_type** | **str** | Specifies an error type(if any) corresponding to this entityId. | [optional] 

## Example

```python
from cohesity_sdk.models.associate_entity_metadata_result_params import AssociateEntityMetadataResultParams

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateEntityMetadataResultParams from a JSON string
associate_entity_metadata_result_params_instance = AssociateEntityMetadataResultParams.from_json(json)
# print the JSON string representation of the object
print(AssociateEntityMetadataResultParams.to_json())

# convert the object into a dict
associate_entity_metadata_result_params_dict = associate_entity_metadata_result_params_instance.to_dict()
# create an instance of AssociateEntityMetadataResultParams from a dict
associate_entity_metadata_result_params_from_dict = AssociateEntityMetadataResultParams.from_dict(associate_entity_metadata_result_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


