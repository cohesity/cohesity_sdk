# HeliosAuditLogSettings

Description of a Helios audit log setting.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_settings** | [**[HeliosAuditLogUserSetting]**](HeliosAuditLogUserSetting.md) | List of users level Helios audit log settings. | [optional] 
**role_settings** | [**[HeliosAuditLogRoleSetting]**](HeliosAuditLogRoleSetting.md) | List of role level Helios audit log settings. | [optional] 
**read_logging** | **bool, none_type** | Toggle global level verbose logging for read events. | [optional]  if omitted the server will use the default value of False
**retention_period_days** | **int, none_type** | Helios Log retention period in days. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


