# AuditLogConfig

Specifies the generic object for audit log configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies if audit log is enabled. | 
**retention_period_days** | **int** | Specifies the audit log retention period in days. Audit logs generated before the period of time specified by retentionPeriodDays are removed from the Cohesity Cluster. | 

## Example

```python
from cohesity_sdk.models.audit_log_config import AuditLogConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogConfig from a JSON string
audit_log_config_instance = AuditLogConfig.from_json(json)
# print the JSON string representation of the object
print(AuditLogConfig.to_json())

# convert the object into a dict
audit_log_config_dict = audit_log_config_instance.to_dict()
# create an instance of AuditLogConfig from a dict
audit_log_config_from_dict = AuditLogConfig.from_dict(audit_log_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


