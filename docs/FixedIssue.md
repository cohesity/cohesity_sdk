# FixedIssue

Specifies the description of a fixed issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies a unique number of the bug. | [optional] 
**release_note** | **str** | Specifies the description of fix made for the issue. | [optional] 

## Example

```python
from cohesity_sdk.models.fixed_issue import FixedIssue

# TODO update the JSON string below
json = "{}"
# create an instance of FixedIssue from a JSON string
fixed_issue_instance = FixedIssue.from_json(json)
# print the JSON string representation of the object
print(FixedIssue.to_json())

# convert the object into a dict
fixed_issue_dict = fixed_issue_instance.to_dict()
# create an instance of FixedIssue from a dict
fixed_issue_from_dict = FixedIssue.from_dict(fixed_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


