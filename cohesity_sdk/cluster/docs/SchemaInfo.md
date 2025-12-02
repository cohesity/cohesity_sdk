# SchemaInfo

Specifies the time series schema info of the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Specifies the id of the entity represented as a string. | [optional] 
**key** | **str** | Specifies the key which is public facing name for metric name. | [optional] 
**metric_name** | **str** | Specifies the Apollo schema metric name. | [optional] 
**schema_name** | **str** | Specifies the name of entity schema such as &#39;ApolloViewBoxStats&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.schema_info import SchemaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaInfo from a JSON string
schema_info_instance = SchemaInfo.from_json(json)
# print the JSON string representation of the object
print(SchemaInfo.to_json())

# convert the object into a dict
schema_info_dict = schema_info_instance.to_dict()
# create an instance of SchemaInfo from a dict
schema_info_from_dict = SchemaInfo.from_dict(schema_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


