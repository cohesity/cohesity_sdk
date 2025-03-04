# CommonUpdatableUserParams

Specifies user properties which can be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the User. | [optional] 
**effective_time_msecs** | **int** | Specifies the epoch time in milliseconds since when the user can login. | [optional] 
**expiry_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster. | [optional] 
**locked** | **bool** | Specifies whether the User is locked. | [optional] 
**restricted** | **bool** | Specifies whether the User is restricted. A restricted user can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 

## Example

```python
from cohesity_sdk.models.common_updatable_user_params import CommonUpdatableUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonUpdatableUserParams from a JSON string
common_updatable_user_params_instance = CommonUpdatableUserParams.from_json(json)
# print the JSON string representation of the object
print(CommonUpdatableUserParams.to_json())

# convert the object into a dict
common_updatable_user_params_dict = common_updatable_user_params_instance.to_dict()
# create an instance of CommonUpdatableUserParams from a dict
common_updatable_user_params_from_dict = CommonUpdatableUserParams.from_dict(common_updatable_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


