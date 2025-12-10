# UpdateAlertResolutionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id_list** | **List[str]** | Specifies the Alerts to resolve, which are specified by Alert Ids. | [optional] 
**resolution_id** | **int** | Specifies Resolution id that will be applied to a new set of Alerts | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_alert_resolution_request import UpdateAlertResolutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlertResolutionRequest from a JSON string
update_alert_resolution_request_instance = UpdateAlertResolutionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAlertResolutionRequest.to_json())

# convert the object into a dict
update_alert_resolution_request_dict = update_alert_resolution_request_instance.to_dict()
# create an instance of UpdateAlertResolutionRequest from a dict
update_alert_resolution_request_from_dict = UpdateAlertResolutionRequest.from_dict(update_alert_resolution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


