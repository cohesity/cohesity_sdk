# SourceHierarchyModificationResult

Result of a single modification request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for failure if the modification was not successful. | [optional] 
**succeeded** | **bool** | Whether this specific modification was successful. | [optional] 
**vcd_result** | [**VCDModificationResult**](VCDModificationResult.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.source_hierarchy_modification_result import SourceHierarchyModificationResult

# TODO update the JSON string below
json = "{}"
# create an instance of SourceHierarchyModificationResult from a JSON string
source_hierarchy_modification_result_instance = SourceHierarchyModificationResult.from_json(json)
# print the JSON string representation of the object
print(SourceHierarchyModificationResult.to_json())

# convert the object into a dict
source_hierarchy_modification_result_dict = source_hierarchy_modification_result_instance.to_dict()
# create an instance of SourceHierarchyModificationResult from a dict
source_hierarchy_modification_result_from_dict = SourceHierarchyModificationResult.from_dict(source_hierarchy_modification_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


