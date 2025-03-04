# NonCurrentVersionExpirationAction

Specifies the Lifecycle Non-current Version Expiration Action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Specifies the number of days an object is non-current before performing the associated action. | [optional] 

## Example

```python
from cohesity_sdk.models.non_current_version_expiration_action import NonCurrentVersionExpirationAction

# TODO update the JSON string below
json = "{}"
# create an instance of NonCurrentVersionExpirationAction from a JSON string
non_current_version_expiration_action_instance = NonCurrentVersionExpirationAction.from_json(json)
# print the JSON string representation of the object
print(NonCurrentVersionExpirationAction.to_json())

# convert the object into a dict
non_current_version_expiration_action_dict = non_current_version_expiration_action_instance.to_dict()
# create an instance of NonCurrentVersionExpirationAction from a dict
non_current_version_expiration_action_from_dict = NonCurrentVersionExpirationAction.from_dict(non_current_version_expiration_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


