# CreateAzureApplicationRequestParams

Specifies the request parameters for creating Azure Applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Specifies the access token for Azure PowerShell Application access. | 
**app_count** | **int** | Specifies the count of Azure application to be created. | 
**existing_microsoft365_app_credentials_list** | [**List[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application credentials already added within the Microsoft365 source. | [optional] 
**microsoft365_region** | **str** | Specifies the region where Office 365 Exchange environment is. | [optional] 
**username** | **str** | Specifies the username to access Microsoft365 source. | 

## Example

```python
from cohesity_sdk.helios.models.create_azure_application_request_params import CreateAzureApplicationRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAzureApplicationRequestParams from a JSON string
create_azure_application_request_params_instance = CreateAzureApplicationRequestParams.from_json(json)
# print the JSON string representation of the object
print(CreateAzureApplicationRequestParams.to_json())

# convert the object into a dict
create_azure_application_request_params_dict = create_azure_application_request_params_instance.to_dict()
# create an instance of CreateAzureApplicationRequestParams from a dict
create_azure_application_request_params_from_dict = CreateAzureApplicationRequestParams.from_dict(create_azure_application_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


