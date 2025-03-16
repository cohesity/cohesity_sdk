# ViewObjectSummary

Specifies the view object summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_views_count** | **int** | Specifies the total views count. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_object_summary import ViewObjectSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewObjectSummary from a JSON string
view_object_summary_instance = ViewObjectSummary.from_json(json)
# print the JSON string representation of the object
print(ViewObjectSummary.to_json())

# convert the object into a dict
view_object_summary_dict = view_object_summary_instance.to_dict()
# create an instance of ViewObjectSummary from a dict
view_object_summary_from_dict = ViewObjectSummary.from_dict(view_object_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


