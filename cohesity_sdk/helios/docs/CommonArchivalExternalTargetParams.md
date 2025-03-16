# CommonArchivalExternalTargetParams

Specifies the common parameters which are specific to Archival purpose type External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption** | [**EncryptionSettings**](EncryptionSettings.md) |  | 
**storage_type** | **str** | Specifies the Storage type of the External Target. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. | 
**target_bandwidth_throttlings** | [**TargetBandwidthThrottlings**](TargetBandwidthThrottlings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_archival_external_target_params import CommonArchivalExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonArchivalExternalTargetParams from a JSON string
common_archival_external_target_params_instance = CommonArchivalExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonArchivalExternalTargetParams.to_json())

# convert the object into a dict
common_archival_external_target_params_dict = common_archival_external_target_params_instance.to_dict()
# create an instance of CommonArchivalExternalTargetParams from a dict
common_archival_external_target_params_from_dict = CommonArchivalExternalTargetParams.from_dict(common_archival_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


