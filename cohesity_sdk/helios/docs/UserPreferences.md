# UserPreferences

Specifies Preferences for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Specifies the locale of the user. Default value is &#39;en-us&#39; | [optional] [default to 'en-us']

## Example

```python
from cohesity_sdk.helios.models.user_preferences import UserPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of UserPreferences from a JSON string
user_preferences_instance = UserPreferences.from_json(json)
# print the JSON string representation of the object
print(UserPreferences.to_json())

# convert the object into a dict
user_preferences_dict = user_preferences_instance.to_dict()
# create an instance of UserPreferences from a dict
user_preferences_from_dict = UserPreferences.from_dict(user_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


