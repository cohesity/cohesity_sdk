# NoSqlObjectProperty

Specifies an Object property as a set of key-value pair for NoSQL objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the key of the property. | 
**value** | **str** | specifies the value of the property. | 

## Example

```python
from cohesity_sdk.models.no_sql_object_property import NoSqlObjectProperty

# TODO update the JSON string below
json = "{}"
# create an instance of NoSqlObjectProperty from a JSON string
no_sql_object_property_instance = NoSqlObjectProperty.from_json(json)
# print the JSON string representation of the object
print(NoSqlObjectProperty.to_json())

# convert the object into a dict
no_sql_object_property_dict = no_sql_object_property_instance.to_dict()
# create an instance of NoSqlObjectProperty from a dict
no_sql_object_property_from_dict = NoSqlObjectProperty.from_dict(no_sql_object_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


