# HeliosAuditLogsEntityTypes

Specifies entity types of audit logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_types** | **List[str]** | Specifies a list of audit logs entity types. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_logs_entity_types import HeliosAuditLogsEntityTypes

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogsEntityTypes from a JSON string
helios_audit_logs_entity_types_instance = HeliosAuditLogsEntityTypes.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogsEntityTypes.to_json())

# convert the object into a dict
helios_audit_logs_entity_types_dict = helios_audit_logs_entity_types_instance.to_dict()
# create an instance of HeliosAuditLogsEntityTypes from a dict
helios_audit_logs_entity_types_from_dict = HeliosAuditLogsEntityTypes.from_dict(helios_audit_logs_entity_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


