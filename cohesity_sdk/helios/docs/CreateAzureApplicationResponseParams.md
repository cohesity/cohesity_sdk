# CreateAzureApplicationResponseParams

Specifies the response parameters containing the Azure apps created within the Microsoft365 domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft365_app_credentials_list** | [**List[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application credentials needed to authenticate &amp; authorize users for Office 365. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_azure_application_response_params import CreateAzureApplicationResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAzureApplicationResponseParams from a JSON string
create_azure_application_response_params_instance = CreateAzureApplicationResponseParams.from_json(json)
# print the JSON string representation of the object
print(CreateAzureApplicationResponseParams.to_json())

# convert the object into a dict
create_azure_application_response_params_dict = create_azure_application_response_params_instance.to_dict()
# create an instance of CreateAzureApplicationResponseParams from a dict
create_azure_application_response_params_from_dict = CreateAzureApplicationResponseParams.from_dict(create_azure_application_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


