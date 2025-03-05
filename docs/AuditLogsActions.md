# AuditLogsActions

Specifies actions of audit logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[str]** | Specifies a list of audit logs actions. | [optional] 

## Example

```python
from cohesity_sdk.models.audit_logs_actions import AuditLogsActions

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogsActions from a JSON string
audit_logs_actions_instance = AuditLogsActions.from_json(json)
# print the JSON string representation of the object
print(AuditLogsActions.to_json())

# convert the object into a dict
audit_logs_actions_dict = audit_logs_actions_instance.to_dict()
# create an instance of AuditLogsActions from a dict
audit_logs_actions_from_dict = AuditLogsActions.from_dict(audit_logs_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


