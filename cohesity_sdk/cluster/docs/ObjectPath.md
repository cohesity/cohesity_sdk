# ObjectPath

Specifies the object path of restore config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_store_path** | [**DataStorePath**](DataStorePath.md) |  | [optional] 
**default_path** | **str** | Specifies the default path of the object path. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_path import ObjectPath

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectPath from a JSON string
object_path_instance = ObjectPath.from_json(json)
# print the JSON string representation of the object
print(ObjectPath.to_json())

# convert the object into a dict
object_path_dict = object_path_instance.to_dict()
# create an instance of ObjectPath from a dict
object_path_from_dict = ObjectPath.from_dict(object_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


