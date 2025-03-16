# HeliosAuditLogSettings

Description of a Helios audit log setting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_logging** | **bool** | Toggle global level verbose logging for read events. | [optional] [default to False]
**retention_period_days** | **int** | Helios Log retention period in days. | [optional] 
**role_settings** | [**List[HeliosAuditLogRoleSetting]**](HeliosAuditLogRoleSetting.md) | List of role level Helios audit log settings. | [optional] 
**user_settings** | [**List[HeliosAuditLogUserSetting]**](HeliosAuditLogUserSetting.md) | List of users level Helios audit log settings. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log_settings import HeliosAuditLogSettings

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogSettings from a JSON string
helios_audit_log_settings_instance = HeliosAuditLogSettings.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogSettings.to_json())

# convert the object into a dict
helios_audit_log_settings_dict = helios_audit_log_settings_instance.to_dict()
# create an instance of HeliosAuditLogSettings from a dict
helios_audit_log_settings_from_dict = HeliosAuditLogSettings.from_dict(helios_audit_log_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


