# CreateAzureApplicationRequestParams

Specifies the request parameters for creating Azure Applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Specifies the access token for Azure Application access. | 
**app_count** | **int** | Specifies the count of Azure application to be created. | 
**azure_tenant_id** | **str** | Specifies the Azure Active Directory tenant ID or domain name. | [optional] 
**certificate_thumbprints** | **List[str]** | Specifies a list of certificate thumbprints. The count of items in this list should be either one or equal to the appCount. If only a single thumbprint is provided, all newly created apps will share the certificate. | [optional] 
**existing_microsoft365_app_credentials_list** | [**List[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application credentials already added within the Microsoft365 source. | [optional] 
**microsoft365_region** | **str** | Specifies the region where Office 365 Exchange environment is. | [optional] 
**o365_app_credentials_list_for_cert_update** | [**List[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies the list of exisiting Microsoft365 azure application credentials for which certificates are to be added/ updated. Each app credential in this list should contain a certificate id. | [optional] 
**update_app_key_only** | **bool** | Specifies whether only secret key for app should be updated during edit call. | [optional] [default to False]
**use_cases** | **List[str]** | The usecases for which the application is to be created. | [optional] 
**username** | **str** | Specifies the username to access Microsoft365 source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_azure_application_request_params import CreateAzureApplicationRequestParams

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


