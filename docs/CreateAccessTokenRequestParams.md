# CreateAccessTokenRequestParams

Specifies the Cohesity credentials required for creating an access token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain the user is logging in to. For a local user the domain is LOCAL. For LDAP/AD user, the domain will map to a LDAP connection string. A user is uniquely identified by a combination of username and domain. LOCAL is the default domain. | [optional] 
**password** | **str** | Specifies the password of the Cohesity user account. | 
**username** | **str** | Specifies the login name of the Cohesity user. | 

## Example

```python
from cohesity_sdk.models.create_access_token_request_params import CreateAccessTokenRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessTokenRequestParams from a JSON string
create_access_token_request_params_instance = CreateAccessTokenRequestParams.from_json(json)
# print the JSON string representation of the object
print(CreateAccessTokenRequestParams.to_json())

# convert the object into a dict
create_access_token_request_params_dict = create_access_token_request_params_instance.to_dict()
# create an instance of CreateAccessTokenRequestParams from a dict
create_access_token_request_params_from_dict = CreateAccessTokenRequestParams.from_dict(create_access_token_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


