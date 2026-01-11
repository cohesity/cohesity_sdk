# ClusterAuditLogConfig

Specifies the Cluster audit log configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool, none_type** | Specifies if audit log is enabled. | 
**retention_period_days** | **int, none_type** | Specifies the audit log retention period in days. Audit logs generated before the period of time specified by retentionPeriodDays are removed from the Cohesity Cluster. | 
**verbose_audit** | **bool, none_type** | Specifies if the Cluster audit logging includes prev value and new value. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


