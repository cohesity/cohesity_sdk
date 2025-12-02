# NotificationRule

Details about the Alert Notification rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** | Name of the notification rule | 
**alert_names** | **[str], none_type** | Alert names that this rule is applicable to | [optional] 
**categories** | **[str], none_type** | Alert categories that this rule is applicable to | [optional] 
**email_delivery_targets** | [**[EmailDeliveryTarget], none_type**](EmailDeliveryTarget.md) | Email configs for the alerts matching this rule | [optional] 
**id** | **int** | Unique id of the notification rule | [optional] [readonly] 
**severities** | **[str]** | Alert severity levels this rule is applicable to | [optional] 
**snmp_enabled** | **bool** | Whether snmp is enabled as part of this notification | [optional] 
**syslog_enabled** | **bool** | Whether syslog is enabled as part of this notification | [optional] 
**tenant_id** | **str, none_type** | Tenant id that this rule is applicable to | [optional] 
**webhook_delivery_targets** | [**[WebhookDeliveryTarget], none_type**](WebhookDeliveryTarget.md) | Webhook configs for the alerts matching this rule | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


