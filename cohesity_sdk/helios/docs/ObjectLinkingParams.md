# ObjectLinkingParams

Specifies the parameters required for linking objects. This is currently used as a part of vm migration workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_map** | [**List[ActionObjectMapping]**](ActionObjectMapping.md) | Specifies the objectMap that will be used to perform bulk actions such as linking and unlinking. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_linking_params import ObjectLinkingParams

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectLinkingParams from a JSON string
object_linking_params_instance = ObjectLinkingParams.from_json(json)
# print the JSON string representation of the object
print(ObjectLinkingParams.to_json())

# convert the object into a dict
object_linking_params_dict = object_linking_params_instance.to_dict()
# create an instance of ObjectLinkingParams from a dict
object_linking_params_from_dict = ObjectLinkingParams.from_dict(object_linking_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


