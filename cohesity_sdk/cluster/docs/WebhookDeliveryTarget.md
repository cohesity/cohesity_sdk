# WebhookDeliveryTarget

Webhook config for the alerts matching this rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curl_options** | **str** | Options for webhook | [optional] 
**webhook_url** | **str** | Destination webhook URL | 

## Example

```python
from cohesity_sdk.cluster.models.webhook_delivery_target import WebhookDeliveryTarget

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryTarget from a JSON string
webhook_delivery_target_instance = WebhookDeliveryTarget.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryTarget.to_json())

# convert the object into a dict
webhook_delivery_target_dict = webhook_delivery_target_instance.to_dict()
# create an instance of WebhookDeliveryTarget from a dict
webhook_delivery_target_from_dict = WebhookDeliveryTarget.from_dict(webhook_delivery_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


