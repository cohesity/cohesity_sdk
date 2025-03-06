# AuditLogs

Sepcifies the audit logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_logs** | [**List[AuditLog]**](AuditLog.md) | Specifies a list of audit logs. | [optional] 
**count** | **int** | Specifies the total number of audit logs that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.audit_logs import AuditLogs

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogs from a JSON string
audit_logs_instance = AuditLogs.from_json(json)
# print the JSON string representation of the object
print(AuditLogs.to_json())

# convert the object into a dict
audit_logs_dict = audit_logs_instance.to_dict()
# create an instance of AuditLogs from a dict
audit_logs_from_dict = AuditLogs.from_dict(audit_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


