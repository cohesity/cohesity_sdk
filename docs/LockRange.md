# LockRange

Specifies details of an entity lock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_exclusive** | **bool** | Specifies if entity lock is exclusive. | [optional] 
**length** | **int** | Specifies the length of an entity lock. | [optional] 
**offset** | **int** | Specifies the offset of an entity lock. | [optional] 

## Example

```python
from cohesity_sdk.models.lock_range import LockRange

# TODO update the JSON string below
json = "{}"
# create an instance of LockRange from a JSON string
lock_range_instance = LockRange.from_json(json)
# print the JSON string representation of the object
print(LockRange.to_json())

# convert the object into a dict
lock_range_dict = lock_range_instance.to_dict()
# create an instance of LockRange from a dict
lock_range_from_dict = LockRange.from_dict(lock_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


