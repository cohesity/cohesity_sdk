# NlmLock

Specifies a NLM lock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the client ID. | [optional] 
**lock_ranges** | [**List[LockRange]**](LockRange.md) | Specifies the list of lock ranges. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.nlm_lock import NlmLock

# TODO update the JSON string below
json = "{}"
# create an instance of NlmLock from a JSON string
nlm_lock_instance = NlmLock.from_json(json)
# print the JSON string representation of the object
print(NlmLock.to_json())

# convert the object into a dict
nlm_lock_dict = nlm_lock_instance.to_dict()
# create an instance of NlmLock from a dict
nlm_lock_from_dict = NlmLock.from_dict(nlm_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


