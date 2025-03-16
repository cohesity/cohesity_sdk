# ProgressSummary

Specifies the progress summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** | Specifies the failed count. | [optional] 
**success** | **int** | Specifies the successful count. | [optional] 
**total** | **int** | Specifies the total count. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.progress_summary import ProgressSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressSummary from a JSON string
progress_summary_instance = ProgressSummary.from_json(json)
# print the JSON string representation of the object
print(ProgressSummary.to_json())

# convert the object into a dict
progress_summary_dict = progress_summary_instance.to_dict()
# create an instance of ProgressSummary from a dict
progress_summary_from_dict = ProgressSummary.from_dict(progress_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


