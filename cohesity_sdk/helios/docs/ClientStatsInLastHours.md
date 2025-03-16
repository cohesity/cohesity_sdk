# ClientStatsInLastHours

Specifies the Client stats for last hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_hours** | **int** | Specifies the time range. | [optional] 
**value** | **int** | Specifies the stats value. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.client_stats_in_last_hours import ClientStatsInLastHours

# TODO update the JSON string below
json = "{}"
# create an instance of ClientStatsInLastHours from a JSON string
client_stats_in_last_hours_instance = ClientStatsInLastHours.from_json(json)
# print the JSON string representation of the object
print(ClientStatsInLastHours.to_json())

# convert the object into a dict
client_stats_in_last_hours_dict = client_stats_in_last_hours_instance.to_dict()
# create an instance of ClientStatsInLastHours from a dict
client_stats_in_last_hours_from_dict = ClientStatsInLastHours.from_dict(client_stats_in_last_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


