# ExpirationAction

Specifies the Lifecycle current version ExpirationAction. Note: All the three fields are mutually exclusive to each other.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_in_usecs** | **int** | Specifies the Timestamp in Usecs for the date when the object is subject to the rule. | [optional] 
**days** | **int** | Specifies the Lifetime in days of the objects that are subject to the rule. | [optional] 
**expired_object_delete_marker** | **bool** | Specifies whether Amazon S3 will remove a delete marker with no non-current versions. If set, the delete marker will be expired. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.expiration_action import ExpirationAction

# TODO update the JSON string below
json = "{}"
# create an instance of ExpirationAction from a JSON string
expiration_action_instance = ExpirationAction.from_json(json)
# print the JSON string representation of the object
print(ExpirationAction.to_json())

# convert the object into a dict
expiration_action_dict = expiration_action_instance.to_dict()
# create an instance of ExpirationAction from a dict
expiration_action_from_dict = ExpirationAction.from_dict(expiration_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


