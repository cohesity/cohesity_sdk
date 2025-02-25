# ViewAliasInfo

View Alias Info is returned as part of list views.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_name** | **str, none_type** | Alias name. | [optional] 
**client_subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 
**enable_filer_audit_log** | **bool, none_type** | This field is currently deprecated. Specifies whether to enable filer audit log on this view alias. This is only used if filer audit logging is enabled in cluster config. | [optional] 
**file_audit_logging_state** | **str, none_type** | Specifies the state of File Audit logging for this Share. Supported types: [Inherited, Enabled, Disabled]. Inherited: Audit log setting is inherited from the  View. Enabled: Audit log is enabled for this Share. Disabled: Audit log is disabled for this Share. | [optional] 
**smb_config** | [**AliasSmbConfig**](AliasSmbConfig.md) |  | [optional] 
**view_path** | **str, none_type** | View path for the alias. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


