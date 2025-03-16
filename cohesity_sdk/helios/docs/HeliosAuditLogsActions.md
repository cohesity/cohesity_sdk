# HeliosAuditLogsActions

Specifies actions of audit logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[str]** | Specifies a list of audit logs actions. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_logs_actions import HeliosAuditLogsActions

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogsActions from a JSON string
helios_audit_logs_actions_instance = HeliosAuditLogsActions.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogsActions.to_json())

# convert the object into a dict
helios_audit_logs_actions_dict = helios_audit_logs_actions_instance.to_dict()
# create an instance of HeliosAuditLogsActions from a dict
helios_audit_logs_actions_from_dict = HeliosAuditLogsActions.from_dict(helios_audit_logs_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


