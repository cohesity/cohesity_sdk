# MissingEntityParams

Specifies the information about missing entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**parent_source_id** | **int** | Specifies the id of the parent source of the object. | [optional] [readonly] 
**parent_source_name** | **str** | Specifies the name of the parent source of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.missing_entity_params import MissingEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of MissingEntityParams from a JSON string
missing_entity_params_instance = MissingEntityParams.from_json(json)
# print the JSON string representation of the object
print(MissingEntityParams.to_json())

# convert the object into a dict
missing_entity_params_dict = missing_entity_params_instance.to_dict()
# create an instance of MissingEntityParams from a dict
missing_entity_params_from_dict = MissingEntityParams.from_dict(missing_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


