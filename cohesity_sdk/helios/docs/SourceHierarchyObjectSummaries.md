# SourceHierarchyObjectSummaries

Specifies a list of Source Hierarchy Object Summaries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[SourceHierarchyObjectSummary]**](SourceHierarchyObjectSummary.md) | Specifies a list of Source Hierarchy Object summaries. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.source_hierarchy_object_summaries import SourceHierarchyObjectSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of SourceHierarchyObjectSummaries from a JSON string
source_hierarchy_object_summaries_instance = SourceHierarchyObjectSummaries.from_json(json)
# print the JSON string representation of the object
print(SourceHierarchyObjectSummaries.to_json())

# convert the object into a dict
source_hierarchy_object_summaries_dict = source_hierarchy_object_summaries_instance.to_dict()
# create an instance of SourceHierarchyObjectSummaries from a dict
source_hierarchy_object_summaries_from_dict = SourceHierarchyObjectSummaries.from_dict(source_hierarchy_object_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


