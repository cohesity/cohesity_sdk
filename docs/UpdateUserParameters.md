# UpdateUserParameters

Specifies User properties to update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the User. | [optional] 
**effective_time_msecs** | **int** | Specifies the epoch time in milliseconds since when the user can login. | [optional] 
**expiry_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster. | [optional] 
**locked** | **bool** | Specifies whether the User is locked. | [optional] 
**restricted** | **bool** | Specifies whether the User is restricted. A restricted user can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 
**local_user_params** | [**LocalUserUpdateParams**](LocalUserUpdateParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.update_user_parameters import UpdateUserParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserParameters from a JSON string
update_user_parameters_instance = UpdateUserParameters.from_json(json)
# print the JSON string representation of the object
print(UpdateUserParameters.to_json())

# convert the object into a dict
update_user_parameters_dict = update_user_parameters_instance.to_dict()
# create an instance of UpdateUserParameters from a dict
update_user_parameters_from_dict = UpdateUserParameters.from_dict(update_user_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


