# ObjectActionRequest

Specifies the request to peform an action on an Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment type of the Object. | 
**vmware_params** | [**VmwareObjectActionParams**](VmwareObjectActionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_action_request import ObjectActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectActionRequest from a JSON string
object_action_request_instance = ObjectActionRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectActionRequest.to_json())

# convert the object into a dict
object_action_request_dict = object_action_request_instance.to_dict()
# create an instance of ObjectActionRequest from a dict
object_action_request_from_dict = ObjectActionRequest.from_dict(object_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


