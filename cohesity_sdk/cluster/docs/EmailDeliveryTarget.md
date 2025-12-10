# EmailDeliveryTarget

Email config for the alerts matching this rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Main recepient email addresses | 
**locale** | **str** | Locale of the email recipient. | [optional] 
**recipient_type** | **str** | Whether to add recipient as To or CC | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.email_delivery_target import EmailDeliveryTarget

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDeliveryTarget from a JSON string
email_delivery_target_instance = EmailDeliveryTarget.from_json(json)
# print the JSON string representation of the object
print(EmailDeliveryTarget.to_json())

# convert the object into a dict
email_delivery_target_dict = email_delivery_target_instance.to_dict()
# create an instance of EmailDeliveryTarget from a dict
email_delivery_target_from_dict = EmailDeliveryTarget.from_dict(email_delivery_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


