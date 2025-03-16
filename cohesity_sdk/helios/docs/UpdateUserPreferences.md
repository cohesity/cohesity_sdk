# UpdateUserPreferences

Updates Preferences for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Specifies the locale of the user. Default value is &#39;en-us&#39; | [optional] [default to 'en-us']
**reset** | **bool** | Reset to default values | [optional] [default to False]

## Example

```python
from cohesity_sdk.helios.models.update_user_preferences import UpdateUserPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPreferences from a JSON string
update_user_preferences_instance = UpdateUserPreferences.from_json(json)
# print the JSON string representation of the object
print(UpdateUserPreferences.to_json())

# convert the object into a dict
update_user_preferences_dict = update_user_preferences_instance.to_dict()
# create an instance of UpdateUserPreferences from a dict
update_user_preferences_from_dict = UpdateUserPreferences.from_dict(update_user_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


