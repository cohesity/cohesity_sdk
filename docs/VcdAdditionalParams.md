# VcdAdditionalParams

Additional params for VCD protection source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcenter_info_list** | [**List[VcdVcenterInfo]**](VcdVcenterInfo.md) | Specifies the list of vCenters associated with this VCD protection source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vcd_additional_params import VcdAdditionalParams

# TODO update the JSON string below
json = "{}"
# create an instance of VcdAdditionalParams from a JSON string
vcd_additional_params_instance = VcdAdditionalParams.from_json(json)
# print the JSON string representation of the object
print(VcdAdditionalParams.to_json())

# convert the object into a dict
vcd_additional_params_dict = vcd_additional_params_instance.to_dict()
# create an instance of VcdAdditionalParams from a dict
vcd_additional_params_from_dict = VcdAdditionalParams.from_dict(vcd_additional_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


