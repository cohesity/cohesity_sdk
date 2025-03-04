# Time

Specifies the time in hours and minutes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | Specifies the hour of this time. | [optional] 
**minute** | **int** | Specifies the minute of this time. | [optional] 

## Example

```python
from cohesity_sdk.models.time import Time

# TODO update the JSON string below
json = "{}"
# create an instance of Time from a JSON string
time_instance = Time.from_json(json)
# print the JSON string representation of the object
print(Time.to_json())

# convert the object into a dict
time_dict = time_instance.to_dict()
# create an instance of Time from a dict
time_from_dict = Time.from_dict(time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


