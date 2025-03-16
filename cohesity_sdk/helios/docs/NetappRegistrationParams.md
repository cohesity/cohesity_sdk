# NetappRegistrationParams

Specifies parameters to register an Netapp Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_up_smb_volumes** | **bool** | Specifies whether or not to back up SMB Volumes. | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | 
**endpoint** | **str** | Specifies the Hostname or IP Address Endpoint for the Netapp Source. | 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**smb_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**source_type** | **str** | Specifies the Netapp source type. Can be either kCluster or kVServer (SVM). | 
**storage_array_snapshot_config** | [**StorageArraySnapshotConfig**](StorageArraySnapshotConfig.md) |  | [optional] 
**storage_array_snapshot_enabled** | **bool** | Specifies if storage array snapshot is enabled or not in the Source. | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.netapp_registration_params import NetappRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetappRegistrationParams from a JSON string
netapp_registration_params_instance = NetappRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(NetappRegistrationParams.to_json())

# convert the object into a dict
netapp_registration_params_dict = netapp_registration_params_instance.to_dict()
# create an instance of NetappRegistrationParams from a dict
netapp_registration_params_from_dict = NetappRegistrationParams.from_dict(netapp_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


