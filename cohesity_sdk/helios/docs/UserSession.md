# UserSession

User session response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Specifies the session id | [optional] 

## Example

```python
from cohesity_sdk.helios.models.user_session import UserSession

# TODO update the JSON string below
json = "{}"
# create an instance of UserSession from a JSON string
user_session_instance = UserSession.from_json(json)
# print the JSON string representation of the object
print(UserSession.to_json())

# convert the object into a dict
user_session_dict = user_session_instance.to_dict()
# create an instance of UserSession from a dict
user_session_from_dict = UserSession.from_dict(user_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


