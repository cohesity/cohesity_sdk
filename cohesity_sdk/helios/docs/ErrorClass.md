# ErrorClass

Specifies a class of error with name and count of that class.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.error_class import ErrorClass

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorClass from a JSON string
error_class_instance = ErrorClass.from_json(json)
# print the JSON string representation of the object
print(ErrorClass.to_json())

# convert the object into a dict
error_class_dict = error_class_instance.to_dict()
# create an instance of ErrorClass from a dict
error_class_from_dict = ErrorClass.from_dict(error_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


