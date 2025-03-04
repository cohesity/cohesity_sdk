# OriginalNetappTargetParams

Specifies the params of the original Netapp recovery target.

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
from cohesity_sdk.models.original_netapp_target_params import OriginalNetappTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalNetappTargetParams from a JSON string
original_netapp_target_params_instance = OriginalNetappTargetParams.from_json(json)
# print the JSON string representation of the object
print(OriginalNetappTargetParams.to_json())

# convert the object into a dict
original_netapp_target_params_dict = original_netapp_target_params_instance.to_dict()
# create an instance of OriginalNetappTargetParams from a dict
original_netapp_target_params_from_dict = OriginalNetappTargetParams.from_dict(original_netapp_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


