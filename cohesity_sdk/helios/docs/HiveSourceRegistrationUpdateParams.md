# HiveSourceRegistrationUpdateParams

Specifies parameters to update registration of Hive source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str, none_type** | IP or hostname of any host from which the Hive configuration file hive-site.xml can be read. | [optional] 
**configuration_directory** | **str, none_type** | The directory containing the hive-site.xml. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationUpdateParamsSshPasswordCredentials**](HbaseSourceRegistrationUpdateParamsSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationUpdateParamsSshPrivateKeyCredentials**](HbaseSourceRegistrationUpdateParamsSshPrivateKeyCredentials.md) |  | [optional] 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this Hive source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


