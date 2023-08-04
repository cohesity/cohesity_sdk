# RegisterOrUpdateKerberosProviderRequest

Specifies the request to register or update a Kerberos Provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm_name** | **str, none_type** | Specifies the realm name. | 
**kdc_servers** | **[str]** | Specifies a list of Key distribution Centre(KDC) Severs. | 
**admin_server** | **str, none_type** | Specifies the admin server used for registration from the list of KDC servers. | 
**host_alias** | **[str]** | Specifies the DNS routable host alias names. | 
**admin_password** | **str, none_type** | Specifies the password of Kerberos admin principal. | 
**id** | **str, none_type** | Specifies the id. | [optional] [readonly] 
**ldap_provider_id** | **int, none_type** | Specifies the LDAP provider id to be mapped | [optional] 
**overwritehost_alias** | **bool, none_type** | Specifies if specified host alias should overwrite existing host alias. | [optional] 
**admin_principal** | **str, none_type** | Specifies the name of the Kerberos admin principal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


