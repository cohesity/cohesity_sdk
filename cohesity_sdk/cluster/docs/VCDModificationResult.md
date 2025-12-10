# VCDModificationResult

Result details for a VCD object modification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urn** | **str** | The URN of the VCD object that was modified or attempted to be modified. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vcd_modification_result import VCDModificationResult

# TODO update the JSON string below
json = "{}"
# create an instance of VCDModificationResult from a JSON string
vcd_modification_result_instance = VCDModificationResult.from_json(json)
# print the JSON string representation of the object
print(VCDModificationResult.to_json())

# convert the object into a dict
vcd_modification_result_dict = vcd_modification_result_instance.to_dict()
# create an instance of VCDModificationResult from a dict
vcd_modification_result_from_dict = VCDModificationResult.from_dict(vcd_modification_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


