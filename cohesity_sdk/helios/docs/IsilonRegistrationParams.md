# IsilonRegistrationParams

Specifies parameters to register an Isilon Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str, none_type** | Specifies the IP Address Endpoint for the Isilon Source. | 
**credentials** | [**Credentials**](Credentials.md) |  | 
**back_up_smb_volumes** | **bool, none_type** | Specifies whether or not to back up SMB Volumes. | [optional] 
**smb_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

