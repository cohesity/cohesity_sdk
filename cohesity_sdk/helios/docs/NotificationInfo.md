# NotificationInfo

Specifies the details of an anomaly notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_strength_threshold** | **int** | Anomaly strength level beyond which notification has to be sent. | [optional] 
**email_config** | [**EmailConfig**](EmailConfig.md) |  | [optional] 
**webhook_config** | [**WebhookConfig**](WebhookConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.notification_info import NotificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationInfo from a JSON string
notification_info_instance = NotificationInfo.from_json(json)
# print the JSON string representation of the object
print(NotificationInfo.to_json())

# convert the object into a dict
notification_info_dict = notification_info_instance.to_dict()
# create an instance of NotificationInfo from a dict
notification_info_from_dict = NotificationInfo.from_dict(notification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


