# SourceHierarchyModificationRequest

Specifies a single modification request for the source hierarchy. Each request operates on a single object. At least one of the environment-specific parameters (vcdModifyParams, etc.) must be provided, corresponding to the source environment type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Specifies the action to be performed on the object. | 
**vcd_modify_params** | [**VCDModifyHierarchyParams**](VCDModifyHierarchyParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.source_hierarchy_modification_request import SourceHierarchyModificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SourceHierarchyModificationRequest from a JSON string
source_hierarchy_modification_request_instance = SourceHierarchyModificationRequest.from_json(json)
# print the JSON string representation of the object
print(SourceHierarchyModificationRequest.to_json())

# convert the object into a dict
source_hierarchy_modification_request_dict = source_hierarchy_modification_request_instance.to_dict()
# create an instance of SourceHierarchyModificationRequest from a dict
source_hierarchy_modification_request_from_dict = SourceHierarchyModificationRequest.from_dict(source_hierarchy_modification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


