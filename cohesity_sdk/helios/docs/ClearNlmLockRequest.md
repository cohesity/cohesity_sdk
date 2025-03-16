# ClearNlmLockRequest

Specifies details required to clear NLM lock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the id of the client, related to which NLM locks needs to be clear. | [optional] 
**file_path** | **str** | Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional] 
**view_name** | **str** | Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.clear_nlm_lock_request import ClearNlmLockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearNlmLockRequest from a JSON string
clear_nlm_lock_request_instance = ClearNlmLockRequest.from_json(json)
# print the JSON string representation of the object
print(ClearNlmLockRequest.to_json())

# convert the object into a dict
clear_nlm_lock_request_dict = clear_nlm_lock_request_instance.to_dict()
# create an instance of ClearNlmLockRequest from a dict
clear_nlm_lock_request_from_dict = ClearNlmLockRequest.from_dict(clear_nlm_lock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


