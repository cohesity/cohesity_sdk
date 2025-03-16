# ResolvedAlertInfo

The infomation of the alert being resolved

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** | Id of the alert | [optional] 
**alert_name** | **str** | Name of the alert being resolved | [optional] 
**cluster_id** | **int** | Id of the cluster which the alert is associated | [optional] 
**resolved_time_usec** | **int** |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.resolved_alert_info import ResolvedAlertInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedAlertInfo from a JSON string
resolved_alert_info_instance = ResolvedAlertInfo.from_json(json)
# print the JSON string representation of the object
print(ResolvedAlertInfo.to_json())

# convert the object into a dict
resolved_alert_info_dict = resolved_alert_info_instance.to_dict()
# create an instance of ResolvedAlertInfo from a dict
resolved_alert_info_from_dict = ResolvedAlertInfo.from_dict(resolved_alert_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


