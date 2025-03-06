# ArchivalExternalTargetParams

Specifies the parameters which are specific to Archival purpose type External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption** | [**EncryptionSettings**](EncryptionSettings.md) |  | 
**storage_type** | **str** | Specifies the Storage type of the External Target. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. | 
**target_bandwidth_throttlings** | [**TargetBandwidthThrottlings**](TargetBandwidthThrottlings.md) |  | [optional] 
**aws_params** | [**ArchivalAwsExternalTargetParams**](ArchivalAwsExternalTargetParams.md) |  | [optional] 
**azure_params** | [**ArchivalAzureExternalTargetParams**](ArchivalAzureExternalTargetParams.md) |  | [optional] 
**gcp_params** | [**ArchivalGcpExternalTargetParams**](ArchivalGcpExternalTargetParams.md) |  | [optional] 
**nas_params** | [**ArchivalNasExternalTargetParams**](ArchivalNasExternalTargetParams.md) |  | [optional] 
**oracle_params** | [**ArchivalOracleExternalTargetParams**](ArchivalOracleExternalTargetParams.md) |  | [optional] 
**qstar_tape_params** | [**ArchivalQstarTapeExternalTargetParams**](ArchivalQstarTapeExternalTargetParams.md) |  | [optional] 
**s3_comp_params** | [**ArchivalS3CompExternalTargetParams**](ArchivalS3CompExternalTargetParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.archival_external_target_params import ArchivalExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalExternalTargetParams from a JSON string
archival_external_target_params_instance = ArchivalExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalExternalTargetParams.to_json())

# convert the object into a dict
archival_external_target_params_dict = archival_external_target_params_instance.to_dict()
# create an instance of ArchivalExternalTargetParams from a dict
archival_external_target_params_from_dict = ArchivalExternalTargetParams.from_dict(archival_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


