# MultipleViewsUpdateSuccessFailureIds

Specifies the list of View Ids which have succeeded/failed during multiple Views Update operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_view_ids** | **List[int]** | List of View Ids that has resulted in a failed update. | [optional] 
**succeeded_view_ids** | **List[int]** | List of View Ids that has resulted in a successful update. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.multiple_views_update_success_failure_ids import MultipleViewsUpdateSuccessFailureIds

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleViewsUpdateSuccessFailureIds from a JSON string
multiple_views_update_success_failure_ids_instance = MultipleViewsUpdateSuccessFailureIds.from_json(json)
# print the JSON string representation of the object
print(MultipleViewsUpdateSuccessFailureIds.to_json())

# convert the object into a dict
multiple_views_update_success_failure_ids_dict = multiple_views_update_success_failure_ids_instance.to_dict()
# create an instance of MultipleViewsUpdateSuccessFailureIds from a dict
multiple_views_update_success_failure_ids_from_dict = MultipleViewsUpdateSuccessFailureIds.from_dict(multiple_views_update_success_failure_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


