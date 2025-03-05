# ObjectPolicy

Specifies the protection policy for protecting an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the id of protection policy. | 
**protection_type** | **str** | Specifies the protection type. | 

## Example

```python
from cohesity_sdk.models.object_policy import ObjectPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectPolicy from a JSON string
object_policy_instance = ObjectPolicy.from_json(json)
# print the JSON string representation of the object
print(ObjectPolicy.to_json())

# convert the object into a dict
object_policy_dict = object_policy_instance.to_dict()
# create an instance of ObjectPolicy from a dict
object_policy_from_dict = ObjectPolicy.from_dict(object_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


