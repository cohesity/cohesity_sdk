# AppResource

Specifies the details about App Resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[ResourceEndpoint]**](ResourceEndpoint.md) | Specifies the information about endpoint associated with this resorce. | [optional] 
**id** | **str** | Specifies the unique id of the app resource. | [optional] 
**type** | **str** | Specifies the type of the app resource. | [optional] 

## Example

```python
from cohesity_sdk.models.app_resource import AppResource

# TODO update the JSON string below
json = "{}"
# create an instance of AppResource from a JSON string
app_resource_instance = AppResource.from_json(json)
# print the JSON string representation of the object
print(AppResource.to_json())

# convert the object into a dict
app_resource_dict = app_resource_instance.to_dict()
# create an instance of AppResource from a dict
app_resource_from_dict = AppResource.from_dict(app_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


