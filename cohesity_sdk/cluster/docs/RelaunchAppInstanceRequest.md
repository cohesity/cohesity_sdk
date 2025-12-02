# RelaunchAppInstanceRequest

Request Body to relaunch app instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**if_failed** | **bool** | Specifies in what condition should the app be relaunched. Set to true to relaunch app only if it has failed | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.relaunch_app_instance_request import RelaunchAppInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelaunchAppInstanceRequest from a JSON string
relaunch_app_instance_request_instance = RelaunchAppInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(RelaunchAppInstanceRequest.to_json())

# convert the object into a dict
relaunch_app_instance_request_dict = relaunch_app_instance_request_instance.to_dict()
# create an instance of RelaunchAppInstanceRequest from a dict
relaunch_app_instance_request_from_dict = RelaunchAppInstanceRequest.from_dict(relaunch_app_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


