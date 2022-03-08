# GenericNasRegistrationParams

Specifies parameters to register GenericNas MountPoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_point** | **str, none_type** | Specifies the MountPoint for Generic NAS Source. | 
**mode** | **str, none_type** | Specifies the mode of the source. &#39;kNfs3&#39; indicates NFS3 mode. &#39;kNfs4_1&#39; indicates NFS4.1 mode. &#39;kCifs1&#39; indicates SMB mode. | 
**description** | **str, none_type** | Specifies the Description for Generic NAS Source. | [optional] 
**skip_validation** | **bool, none_type** | Specifies if validation has to be skipped while registering the mount point. | [optional] 
**smb_mount_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


