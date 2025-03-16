# HeliosAuditLogRoleSetting

Helios Audit log settings role properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_logging** | **bool** | Toggle verbose logging for read events. If user is assigned multiple roles, then \&quot;OR\&quot; of all valid readLogging is used. | [default to False]
**role_name** | **str** | Role Name. | 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log_role_setting import HeliosAuditLogRoleSetting

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogRoleSetting from a JSON string
helios_audit_log_role_setting_instance = HeliosAuditLogRoleSetting.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogRoleSetting.to_json())

# convert the object into a dict
helios_audit_log_role_setting_dict = helios_audit_log_role_setting_instance.to_dict()
# create an instance of HeliosAuditLogRoleSetting from a dict
helios_audit_log_role_setting_from_dict = HeliosAuditLogRoleSetting.from_dict(helios_audit_log_role_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


