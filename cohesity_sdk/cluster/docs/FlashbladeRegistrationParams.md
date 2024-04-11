# FlashbladeRegistrationParams

Specifies parameters to register an Flashblade Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str, none_type** | Specifies the API Token of the Flashblade Source | 
**endpoint** | **str, none_type** | Specifies the Hostname or IP Address Endpoint for the Flashblade Source. | 
**back_up_smb_volumes** | **bool, none_type** | Specifies whether or not to back up SMB Volumes. | [optional] 
**smb_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

