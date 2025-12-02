# VCDModifyHierarchyParams

VCD specific parameters for modifying an object in a source hierarchy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urn** | **str** | Specifies the URN of the VCD object. | 

## Example

```python
from cohesity_sdk.cluster.models.vcd_modify_hierarchy_params import VCDModifyHierarchyParams

# TODO update the JSON string below
json = "{}"
# create an instance of VCDModifyHierarchyParams from a JSON string
vcd_modify_hierarchy_params_instance = VCDModifyHierarchyParams.from_json(json)
# print the JSON string representation of the object
print(VCDModifyHierarchyParams.to_json())

# convert the object into a dict
vcd_modify_hierarchy_params_dict = vcd_modify_hierarchy_params_instance.to_dict()
# create an instance of VCDModifyHierarchyParams from a dict
vcd_modify_hierarchy_params_from_dict = VCDModifyHierarchyParams.from_dict(vcd_modify_hierarchy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


