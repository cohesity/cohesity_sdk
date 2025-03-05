# OriginalIsilonTargetParams

Specifies the params of the original Isilon recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other volumes if one of the volumes fails to recover. Default value is false. | [optional] 
**encryption_enabled** | **bool** | Specifies whether encryption should be enabled during recovery. | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**overwrite_existing_file** | **bool** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**preserve_file_attributes** | **bool** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.original_isilon_target_params import OriginalIsilonTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalIsilonTargetParams from a JSON string
original_isilon_target_params_instance = OriginalIsilonTargetParams.from_json(json)
# print the JSON string representation of the object
print(OriginalIsilonTargetParams.to_json())

# convert the object into a dict
original_isilon_target_params_dict = original_isilon_target_params_instance.to_dict()
# create an instance of OriginalIsilonTargetParams from a dict
original_isilon_target_params_from_dict = OriginalIsilonTargetParams.from_dict(original_isilon_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


