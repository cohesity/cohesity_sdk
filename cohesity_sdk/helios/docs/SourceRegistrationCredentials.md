# SourceRegistrationCredentials

Specifies the credentials of a source registration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str, none_type** | Specifies the username used to register a source. | [optional] 
**password** | **str, none_type** | Specifies the password used to register a source. | [optional] 
**smb_credentials** | [**SmbCredentials**](SmbCredentials.md) |  | [optional] 
**vcenters** | [**[VcenterCredentialInfo]**](VcenterCredentialInfo.md) | Specifies the list of child vcenter credentials. This will only be populated in the case of VCD. | [optional] 
**office365_app_credentials_list** | [**[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of office365 azure application credentials needed to authenticate &amp; authorize users. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


