# ModelSchema

Specifies the metric data point where public data metric as key and the schema defined metric name as value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Specifies the id of the entity. | [optional] 
**metric_name** | **str** | Specifies the name of schema metric. | [optional] 
**schema_name** | **str** | Specifies the name of the schema. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print(ModelSchema.to_json())

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_from_dict = ModelSchema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


