# UserSessionsCount

Specifies the sessions count for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions_count** | **int** | Specifies the number of sessions for the user. | [optional] 
**sid** | **str** | Specifies the user sid. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.user_sessions_count import UserSessionsCount

# TODO update the JSON string below
json = "{}"
# create an instance of UserSessionsCount from a JSON string
user_sessions_count_instance = UserSessionsCount.from_json(json)
# print the JSON string representation of the object
print(UserSessionsCount.to_json())

# convert the object into a dict
user_sessions_count_dict = user_sessions_count_instance.to_dict()
# create an instance of UserSessionsCount from a dict
user_sessions_count_from_dict = UserSessionsCount.from_dict(user_sessions_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


