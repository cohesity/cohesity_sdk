# RelaunchSystemAppRequest

Request Body to relaunch system app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanup** | **bool** | Specifies whether CleanupCompletedAck should be set on app orchestrator | [optional] 
**if_failed** | **bool** | Specifies in what condition should the app be relaunched. Set to true to relaunch system app only if it has failed | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.relaunch_system_app_request import RelaunchSystemAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelaunchSystemAppRequest from a JSON string
relaunch_system_app_request_instance = RelaunchSystemAppRequest.from_json(json)
# print the JSON string representation of the object
print(RelaunchSystemAppRequest.to_json())

# convert the object into a dict
relaunch_system_app_request_dict = relaunch_system_app_request_instance.to_dict()
# create an instance of RelaunchSystemAppRequest from a dict
relaunch_system_app_request_from_dict = RelaunchSystemAppRequest.from_dict(relaunch_system_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


