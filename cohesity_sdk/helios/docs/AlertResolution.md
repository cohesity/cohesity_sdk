# AlertResolution

Provides Resolution details and the list of Alerts resolved

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Specifies account id of the user who create the resolution | [optional] 
**created_time_usecs** | **int** | Specifies unix epoch timestamp (in microseconds) when the resolution is created. | [optional] 
**description** | **str** | Specifies the full description about the Resolution. | [optional] 
**external_key** | **str** | Specifies the external key assigned outside of helios, with the form of \&quot;clusterid:resolutionid\&quot; | [optional] 
**resolution_id** | **str** | Specifies the unique reslution id assigned in helios. | [optional] 
**resolution_name** | **str** | Specifies the unique name of the resolution. | [optional] 
**resolved_alerts** | [**List[ResolvedAlertInfo]**](ResolvedAlertInfo.md) |  | [optional] 
**silence_minutes** | **int** | Specifies the time duration (in minutes) for silencing alerts. If unspecified or set zero, a silence rule will be created with default expiry time. No silence rule will be created if value &lt; 0. | [optional] 
**tenant_id** | **str** | Specifies tenant id of the user who create the resolution | [optional] 

## Example

```python
from cohesity_sdk.helios.models.alert_resolution import AlertResolution

# TODO update the JSON string below
json = "{}"
# create an instance of AlertResolution from a JSON string
alert_resolution_instance = AlertResolution.from_json(json)
# print the JSON string representation of the object
print(AlertResolution.to_json())

# convert the object into a dict
alert_resolution_dict = alert_resolution_instance.to_dict()
# create an instance of AlertResolution from a dict
alert_resolution_from_dict = AlertResolution.from_dict(alert_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


