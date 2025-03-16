# UserId

Specifies the User Id type. Either sid or unixUid should be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sid** | **str** | Specifies the user sid. | [optional] 
**unix_uid** | **int** | Specifies the unix Uid. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.user_id import UserId

# TODO update the JSON string below
json = "{}"
# create an instance of UserId from a JSON string
user_id_instance = UserId.from_json(json)
# print the JSON string representation of the object
print(UserId.to_json())

# convert the object into a dict
user_id_dict = user_id_instance.to_dict()
# create an instance of UserId from a dict
user_id_from_dict = UserId.from_dict(user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


