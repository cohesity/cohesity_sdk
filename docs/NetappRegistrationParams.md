# NetappRegistrationParams

Specifies parameters to register an Netapp Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | 
**endpoint** | **str, none_type** | Specifies the Hostname or IP Address Endpoint for the Netapp Source. | 
**source_type** | **str, none_type** | Specifies the Netapp source type. Can be either kCluster or kVServer (SVM). | 
**back_up_smb_volumes** | **bool, none_type** | Specifies whether or not to back up SMB Volumes. | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**smb_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**storage_array_snapshot_config** | [**StorageArraySnapshotConfig**](StorageArraySnapshotConfig.md) |  | [optional] 
**storage_array_snapshot_enabled** | **bool, none_type** | Specifies if storage array snapshot is enabled or not in the Source. | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


