# ActiveSessionsCountParams

Specifies the number of sessions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions_per_user** | [**List[UserSessionsCount]**](UserSessionsCount.md) | Specifies the sessions count per user. | [optional] 
**total_sessions_count** | **int** | Specifies the aggregated sessions count for the user sessions returned. If sids are not given this returns the total system wide sessions count and if the sids are given, this returns the total sessions count for the given sids. | [optional] 

## Example

```python
from cohesity_sdk.models.active_sessions_count_params import ActiveSessionsCountParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveSessionsCountParams from a JSON string
active_sessions_count_params_instance = ActiveSessionsCountParams.from_json(json)
# print the JSON string representation of the object
print(ActiveSessionsCountParams.to_json())

# convert the object into a dict
active_sessions_count_params_dict = active_sessions_count_params_instance.to_dict()
# create an instance of ActiveSessionsCountParams from a dict
active_sessions_count_params_from_dict = ActiveSessionsCountParams.from_dict(active_sessions_count_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


