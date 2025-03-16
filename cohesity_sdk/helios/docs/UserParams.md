# UserParams

Specifies a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the User. | [optional] 
**effective_time_msecs** | **int** | Specifies the epoch time in milliseconds since when the user can login. | [optional] 
**expiry_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster. | [optional] 
**locked** | **bool** | Specifies whether the User is locked. | [optional] 
**restricted** | **bool** | Specifies whether the User is restricted. A restricted user can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 
**created_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user account was created. | [optional] [readonly] 
**domain** | **str** | Specifies the domain of the user. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local users on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain. | [optional] [readonly] 
**force_password_change** | **bool** | Specifies if the user must change password. | [optional] [readonly] 
**last_login_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user last logged in successfully. | [optional] [readonly] 
**last_updated_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user account was last modified. | [optional] [readonly] 
**local_user_params** | **object** | Specifies the LOCAL user properties. This field is required when adding a new LOCAL Cohesity User. | [optional] 
**locked_reason** | **str** | Specifies the reason for locking the User. | [optional] [readonly] 
**other_groups** | **List[str]** | Specifies additional groups the User may belong to. | [optional] [readonly] 
**primary_group** | **str** | Specifies the primary group of the User. Primary group is used for file access. | [optional] [readonly] 
**s3_account_params** | **object** | Specifies the S3 Account parameters of the User. | [optional] 
**sid** | **str** | Specifies the sid of the User. | [optional] [readonly] 
**tenant_id** | **str** | Specifies the tenant id of the User. | [optional] 
**username** | **str** | Specifies the username. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.user_params import UserParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserParams from a JSON string
user_params_instance = UserParams.from_json(json)
# print the JSON string representation of the object
print(UserParams.to_json())

# convert the object into a dict
user_params_dict = user_params_instance.to_dict()
# create an instance of UserParams from a dict
user_params_from_dict = UserParams.from_dict(user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


