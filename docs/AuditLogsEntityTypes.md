# AuditLogsEntityTypes

Specifies entity types of audit logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_types** | **List[str]** | Specifies a list of audit logs entity types. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.audit_logs_entity_types import AuditLogsEntityTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogsEntityTypes from a JSON string
audit_logs_entity_types_instance = AuditLogsEntityTypes.from_json(json)
# print the JSON string representation of the object
print(AuditLogsEntityTypes.to_json())

# convert the object into a dict
audit_logs_entity_types_dict = audit_logs_entity_types_instance.to_dict()
# create an instance of AuditLogsEntityTypes from a dict
audit_logs_entity_types_from_dict = AuditLogsEntityTypes.from_dict(audit_logs_entity_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


