# UpdateShareParam

Specifies the parameter to update a Share.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_filer_audit_logging** | **bool, none_type** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**smb_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | SMB config for the alias (share). | [optional] 
**client_subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


