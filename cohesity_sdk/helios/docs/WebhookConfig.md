# WebhookConfig

Specifies the webhook config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_alerts** | **int** | The maximum number of alerts to include in a single webhook message, by default all alerts matched are included. | [optional] 
**options** | **str** | Options for webhook. | [optional] 
**url** | **str** | Destination webhook URL. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.webhook_config import WebhookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookConfig from a JSON string
webhook_config_instance = WebhookConfig.from_json(json)
# print the JSON string representation of the object
print(WebhookConfig.to_json())

# convert the object into a dict
webhook_config_dict = webhook_config_instance.to_dict()
# create an instance of WebhookConfig from a dict
webhook_config_from_dict = WebhookConfig.from_dict(webhook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


