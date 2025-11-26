# UpdateShareParam

Specifies the parameter to update a Share.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 
**enable_filer_audit_logging** | **bool, none_type** | This field is currently deprecated. Specifies if Filer Audit Logging is enabled for this Share. | [optional] 
**file_audit_logging_state** | **str, none_type** | Specifies the state of File Audit logging for this Share. Inherited: Audit log setting is inherited from the  View. Enabled: Audit log is enabled for this Share. Disabled: Audit log is disabled for this Share. | [optional] 
**smb_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | SMB config for the alias (share). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


