# AddedPrincipalResponseObject

Specifies the principals added for the user or group on the Cohesity Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time_msecs** | **int** | Specifies the epoch time in milliseconds when the principal was added to the Cohesity Cluster. | [optional] 
**principal_type** | **str** | Specifies the category of the user or group being added to the Cohesity Cluster. | [optional] 
**sid** | **str** | Specifies the unique Security ID (SID) of the principal associated with the group or user. | [optional] 
**sso_user_principal_details** | [**List[SSOUserPrincipal]**](SSOUserPrincipal.md) | Specifies the details of the SSO user added to the Cohesity Cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.added_principal_response_object import AddedPrincipalResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of AddedPrincipalResponseObject from a JSON string
added_principal_response_object_instance = AddedPrincipalResponseObject.from_json(json)
# print the JSON string representation of the object
print(AddedPrincipalResponseObject.to_json())

# convert the object into a dict
added_principal_response_object_dict = added_principal_response_object_instance.to_dict()
# create an instance of AddedPrincipalResponseObject from a dict
added_principal_response_object_from_dict = AddedPrincipalResponseObject.from_dict(added_principal_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


