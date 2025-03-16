# GetNlmLocksResult

Specifies the list of NLM locks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str** | Specifies the pagination cookie. | [optional] 
**file_nlm_locks** | [**List[FileNlmLocks]**](FileNlmLocks.md) | Specifies the list of NLM locks. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_nlm_locks_result import GetNlmLocksResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetNlmLocksResult from a JSON string
get_nlm_locks_result_instance = GetNlmLocksResult.from_json(json)
# print the JSON string representation of the object
print(GetNlmLocksResult.to_json())

# convert the object into a dict
get_nlm_locks_result_dict = get_nlm_locks_result_instance.to_dict()
# create an instance of GetNlmLocksResult from a dict
get_nlm_locks_result_from_dict = GetNlmLocksResult.from_dict(get_nlm_locks_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


