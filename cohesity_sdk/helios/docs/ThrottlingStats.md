# ThrottlingStats

Specifies the timestamp and corresponding metric values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_time** | **int** | Specifies the time spent idle due to throttling. | [optional] 
**num_api_calls** | **int** | Specifies the total number of API calls made to source. | [optional] 
**num_bytes_read** | **int** | Specifies the total bytes read from source. | [optional] 
**timestamp** | **int** | Specifies the timestamp in milliseconds since the epoch when the stat was recorded. | [optional] 
**total_response_time** | **int** | Specifies the time spent to complete API call. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.throttling_stats import ThrottlingStats

# TODO update the JSON string below
json = "{}"
# create an instance of ThrottlingStats from a JSON string
throttling_stats_instance = ThrottlingStats.from_json(json)
# print the JSON string representation of the object
print(ThrottlingStats.to_json())

# convert the object into a dict
throttling_stats_dict = throttling_stats_instance.to_dict()
# create an instance of ThrottlingStats from a dict
throttling_stats_from_dict = ThrottlingStats.from_dict(throttling_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


