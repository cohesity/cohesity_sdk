# NotificationRule

Details about the Alert Notification rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_names** | **List[str]** | Alert names that this rule is applicable to | [optional] 
**categories** | **List[str]** | Alert categories that this rule is applicable to | [optional] 
**email_delivery_targets** | [**List[EmailDeliveryTarget]**](EmailDeliveryTarget.md) | Email configs for the alerts matching this rule | [optional] 
**id** | **int** | Unique id of the notification rule | [optional] [readonly] 
**rule_name** | **str** | Name of the notification rule | 
**severities** | **List[str]** | Alert severity levels this rule is applicable to | [optional] 
**snmp_enabled** | **bool** | Whether snmp is enabled as part of this notification | [optional] 
**syslog_enabled** | **bool** | Whether syslog is enabled as part of this notification | [optional] 
**tenant_id** | **str** | Tenant id that this rule is applicable to | [optional] 
**webhook_delivery_targets** | [**List[WebhookDeliveryTarget]**](WebhookDeliveryTarget.md) | Webhook configs for the alerts matching this rule | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.notification_rule import NotificationRule

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRule from a JSON string
notification_rule_instance = NotificationRule.from_json(json)
# print the JSON string representation of the object
print(NotificationRule.to_json())

# convert the object into a dict
notification_rule_dict = notification_rule_instance.to_dict()
# create an instance of NotificationRule from a dict
notification_rule_from_dict = NotificationRule.from_dict(notification_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


