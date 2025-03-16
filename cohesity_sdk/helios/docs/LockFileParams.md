# LockFileParams

Specifies the parameters to lock a file in a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_timestamp_msecs** | **int** | Specifies a definite timestamp in milliseconds for retaining the file or to extend it&#39;s expiry timestamp. | 
**file_path** | **str** | Specifies the file path that needs to be locked. | 

## Example

```python
from cohesity_sdk.helios.models.lock_file_params import LockFileParams

# TODO update the JSON string below
json = "{}"
# create an instance of LockFileParams from a JSON string
lock_file_params_instance = LockFileParams.from_json(json)
# print the JSON string representation of the object
print(LockFileParams.to_json())

# convert the object into a dict
lock_file_params_dict = lock_file_params_instance.to_dict()
# create an instance of LockFileParams from a dict
lock_file_params_from_dict = LockFileParams.from_dict(lock_file_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


