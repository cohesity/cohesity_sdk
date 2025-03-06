# CreateUserParameters

Specifies the parameters to create a new Cohesity User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_smb_access_token** | **bool** | Specifies whether the SMB access token is to be set for the user. | [optional] 
**description** | **str** | Specifies the description of the User. | [optional] 
**domain** | **str** | Specifies the domain of the user. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local users on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain. | 
**effective_time_msecs** | **int** | Specifies the epoch time in milliseconds since when the user can login. | [optional] 
**expiry_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster. | [optional] 
**local_user_params** | [**LocalUserParams**](LocalUserParams.md) |  | [optional] 
**locked** | **bool** | Specifies whether the User is locked. | [optional] 
**other_groups** | **List[str]** | Specifies additional groups the User may belong to. | [optional] [readonly] 
**primary_group** | **str** | Specifies the primary group of the User. Primary group is used for file access. | [optional] [readonly] 
**restricted** | **bool** | Specifies whether the User is restricted. A restricted user can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 
**username** | **str** | Specifies the username. | 

## Example

```python
from cohesity_sdk.cluster.models.create_user_parameters import CreateUserParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserParameters from a JSON string
create_user_parameters_instance = CreateUserParameters.from_json(json)
# print the JSON string representation of the object
print(CreateUserParameters.to_json())

# convert the object into a dict
create_user_parameters_dict = create_user_parameters_instance.to_dict()
# create an instance of CreateUserParameters from a dict
create_user_parameters_from_dict = CreateUserParameters.from_dict(create_user_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


