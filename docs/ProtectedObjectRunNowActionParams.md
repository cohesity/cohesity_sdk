# ProtectedObjectRunNowActionParams

Specifies the request parameters for RunNow action on Protected objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[RunNowActionObjectLevelParams]**](RunNowActionObjectLevelParams.md) | Specifies the list of objects to perform an action. If provided object id is not explicitly protected by object protection, then given action will not be performed on that. | [optional] 
**run_label** | **str** | Specifies a label with which this run is created. Only applicable for user triggered protect now action. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protected_object_run_now_action_params import ProtectedObjectRunNowActionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectRunNowActionParams from a JSON string
protected_object_run_now_action_params_instance = ProtectedObjectRunNowActionParams.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectRunNowActionParams.to_json())

# convert the object into a dict
protected_object_run_now_action_params_dict = protected_object_run_now_action_params_instance.to_dict()
# create an instance of ProtectedObjectRunNowActionParams from a dict
protected_object_run_now_action_params_from_dict = ProtectedObjectRunNowActionParams.from_dict(protected_object_run_now_action_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


