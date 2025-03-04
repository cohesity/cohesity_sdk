# VMWareCDPFilterParams

Specifies the parameters to download VMware CDP IO filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esxi_version** | **str** | Specifies the version of the ESXi host where filter needs to be installed. | 

## Example

```python
from cohesity_sdk.models.vm_ware_cdp_filter_params import VMWareCDPFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of VMWareCDPFilterParams from a JSON string
vm_ware_cdp_filter_params_instance = VMWareCDPFilterParams.from_json(json)
# print the JSON string representation of the object
print(VMWareCDPFilterParams.to_json())

# convert the object into a dict
vm_ware_cdp_filter_params_dict = vm_ware_cdp_filter_params_instance.to_dict()
# create an instance of VMWareCDPFilterParams from a dict
vm_ware_cdp_filter_params_from_dict = VMWareCDPFilterParams.from_dict(vm_ware_cdp_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


