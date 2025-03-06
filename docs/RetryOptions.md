# RetryOptions

Retry Options of a Protection Policy when a Protection Group run fails.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retries** | **int** | Specifies the number of times to retry capturing Snapshots before the Protection Group Run fails. | [optional] 
**retry_interval_mins** | **int** | Specifies the number of minutes before retrying a failed Protection Group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.retry_options import RetryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RetryOptions from a JSON string
retry_options_instance = RetryOptions.from_json(json)
# print the JSON string representation of the object
print(RetryOptions.to_json())

# convert the object into a dict
retry_options_dict = retry_options_instance.to_dict()
# create an instance of RetryOptions from a dict
retry_options_from_dict = RetryOptions.from_dict(retry_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


