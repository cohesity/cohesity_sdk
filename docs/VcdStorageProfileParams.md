# VcdStorageProfileParams

Specifies the parameters of a VCD storage profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the storage profile. | [optional] [readonly] 
**vcd_uuid** | **str** | Specifies the UUID assigned by the VCD to the storage profile. | 

## Example

```python
from cohesity_sdk.cluster.models.vcd_storage_profile_params import VcdStorageProfileParams

# TODO update the JSON string below
json = "{}"
# create an instance of VcdStorageProfileParams from a JSON string
vcd_storage_profile_params_instance = VcdStorageProfileParams.from_json(json)
# print the JSON string representation of the object
print(VcdStorageProfileParams.to_json())

# convert the object into a dict
vcd_storage_profile_params_dict = vcd_storage_profile_params_instance.to_dict()
# create an instance of VcdStorageProfileParams from a dict
vcd_storage_profile_params_from_dict = VcdStorageProfileParams.from_dict(vcd_storage_profile_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


