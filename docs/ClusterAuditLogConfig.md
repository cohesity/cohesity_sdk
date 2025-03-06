# ClusterAuditLogConfig

Specifies the Cluster audit log configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies if audit log is enabled. | 
**retention_period_days** | **int** | Specifies the audit log retention period in days. Audit logs generated before the period of time specified by retentionPeriodDays are removed from the Cohesity Cluster. | 
**verbose_audit** | **bool** | Specifies if the Cluster audit logging includes prev value and new value. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_audit_log_config import ClusterAuditLogConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAuditLogConfig from a JSON string
cluster_audit_log_config_instance = ClusterAuditLogConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterAuditLogConfig.to_json())

# convert the object into a dict
cluster_audit_log_config_dict = cluster_audit_log_config_instance.to_dict()
# create an instance of ClusterAuditLogConfig from a dict
cluster_audit_log_config_from_dict = ClusterAuditLogConfig.from_dict(cluster_audit_log_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


