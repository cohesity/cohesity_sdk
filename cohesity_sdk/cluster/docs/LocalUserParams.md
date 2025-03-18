# LocalUserParams

Specifies properties for LOCAL cohesity user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Specifies the email address of the User. | [optional] 
**groups** | **List[str]** | Specifies additional groups the User may belong to. | [optional] [readonly] 
**password** | **str** | Specifies the password of the User. | [optional] 
**primary_group** | **str** | Specifies the primary group of the User. Primary group is used for file access. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.local_user_params import LocalUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of LocalUserParams from a JSON string
local_user_params_instance = LocalUserParams.from_json(json)
# print the JSON string representation of the object
print(LocalUserParams.to_json())

# convert the object into a dict
local_user_params_dict = local_user_params_instance.to_dict()
# create an instance of LocalUserParams from a dict
local_user_params_from_dict = LocalUserParams.from_dict(local_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


