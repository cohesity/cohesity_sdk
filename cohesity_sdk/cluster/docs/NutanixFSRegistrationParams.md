# NutanixFSRegistrationParams

Specifies parameters to register an NutanixFS Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_up_smb_volumes** | **bool** | Specifies whether or not to back up SMB Volumes. | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | 
**endpoint** | **str** | Specifies the Hostname or IP Address Endpoint for the NutanixFS Source. | 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**smb_credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**source_type** | **str** | Specifies the NutanixFS source type. Can be either kPrismCentral or kPrismElement or kFileServer or kMountTarget. | 
**storage_array_snapshot_config** | [**StorageArraySnapshotConfig**](StorageArraySnapshotConfig.md) |  | [optional] 
**storage_array_snapshot_enabled** | **bool** | Specifies if storage array snapshot is enabled or not in the Source. | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.nutanix_fs_registration_params import NutanixFSRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of NutanixFSRegistrationParams from a JSON string
nutanix_fs_registration_params_instance = NutanixFSRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(NutanixFSRegistrationParams.to_json())

# convert the object into a dict
nutanix_fs_registration_params_dict = nutanix_fs_registration_params_instance.to_dict()
# create an instance of NutanixFSRegistrationParams from a dict
nutanix_fs_registration_params_from_dict = NutanixFSRegistrationParams.from_dict(nutanix_fs_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


