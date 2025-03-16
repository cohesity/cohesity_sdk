# HeliosAuditLogUserSetting

Helios Audit log settings user properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_logging** | **bool** | Toggle verbose logging for read events. | [default to False]
**user_sid** | **str** | Salesforce user id. | 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log_user_setting import HeliosAuditLogUserSetting

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogUserSetting from a JSON string
helios_audit_log_user_setting_instance = HeliosAuditLogUserSetting.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogUserSetting.to_json())

# convert the object into a dict
helios_audit_log_user_setting_dict = helios_audit_log_user_setting_instance.to_dict()
# create an instance of HeliosAuditLogUserSetting from a dict
helios_audit_log_user_setting_from_dict = HeliosAuditLogUserSetting.from_dict(helios_audit_log_user_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


