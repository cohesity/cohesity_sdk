# FileNlmLocks

Specifies NLM locks per file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | [**FileId**](FileId.md) |  | [optional] 
**nlm_locks** | [**List[NlmLock]**](NlmLock.md) | Specifies the list of NLM locks. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.file_nlm_locks import FileNlmLocks

# TODO update the JSON string below
json = "{}"
# create an instance of FileNlmLocks from a JSON string
file_nlm_locks_instance = FileNlmLocks.from_json(json)
# print the JSON string representation of the object
print(FileNlmLocks.to_json())

# convert the object into a dict
file_nlm_locks_dict = file_nlm_locks_instance.to_dict()
# create an instance of FileNlmLocks from a dict
file_nlm_locks_from_dict = FileNlmLocks.from_dict(file_nlm_locks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


