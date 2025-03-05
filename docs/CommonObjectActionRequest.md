# CommonObjectActionRequest

Specifies the common request parameters for performing an action on Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment type of the Object. | 

## Example

```python
from cohesity_sdk.models.common_object_action_request import CommonObjectActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommonObjectActionRequest from a JSON string
common_object_action_request_instance = CommonObjectActionRequest.from_json(json)
# print the JSON string representation of the object
print(CommonObjectActionRequest.to_json())

# convert the object into a dict
common_object_action_request_dict = common_object_action_request_instance.to_dict()
# create an instance of CommonObjectActionRequest from a dict
common_object_action_request_from_dict = CommonObjectActionRequest.from_dict(common_object_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


