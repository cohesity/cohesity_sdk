# DeleteAzureApplicationRequestParams

Specifies the request parameters for deleting Azure Applications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Specifies the access token for Azure Application access. | 
**azure_applications_list** | [**List[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application already created within the Microsoft365 source. | 
**azure_tenant_id** | **str** | Specifies the Azure Active Directory tenant ID or domain name. | 
**skip_client_id_verification** | **bool** | Specifies whether to skip client Id verification on the passed access token. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.delete_azure_application_request_params import DeleteAzureApplicationRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAzureApplicationRequestParams from a JSON string
delete_azure_application_request_params_instance = DeleteAzureApplicationRequestParams.from_json(json)
# print the JSON string representation of the object
print(DeleteAzureApplicationRequestParams.to_json())

# convert the object into a dict
delete_azure_application_request_params_dict = delete_azure_application_request_params_instance.to_dict()
# create an instance of DeleteAzureApplicationRequestParams from a dict
delete_azure_application_request_params_from_dict = DeleteAzureApplicationRequestParams.from_dict(delete_azure_application_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


