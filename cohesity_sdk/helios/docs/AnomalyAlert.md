# AnomalyAlert

Specifies the anomaly alert threshold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_info** | [**NotificationInfo**](NotificationInfo.md) |  | [optional] 
**tagging_info** | [**TaggingInfo**](TaggingInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.anomaly_alert import AnomalyAlert

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyAlert from a JSON string
anomaly_alert_instance = AnomalyAlert.from_json(json)
# print the JSON string representation of the object
print(AnomalyAlert.to_json())

# convert the object into a dict
anomaly_alert_dict = anomaly_alert_instance.to_dict()
# create an instance of AnomalyAlert from a dict
anomaly_alert_from_dict = AnomalyAlert.from_dict(anomaly_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


