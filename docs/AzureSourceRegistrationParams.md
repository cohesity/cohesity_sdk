# AzureSourceRegistrationParams

Specifies the paramaters to register an Azure source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_credentials** | [**List[AzureApplicationCredentials]**](AzureApplicationCredentials.md) | Specifies the credentials for a list of applications from azure active directory. | [optional] 
**azure_tenant_id** | **str** | Specifies Tenant Id of the active directory of Azure account. Accpets both Azure tanant Id and tenant domain name. | [optional] 
**registration_level** | **str** | Specifies whether the registration is at tenant level or subscription level. | 
**registration_workflow** | **str** | Specifies whether the type of registration is express or manual. | 
**subscription_details** | [**List[AzureSubscription]**](AzureSubscription.md) | Specifies the list subscription ids to be registered. | [optional] 
**use_cases** | **List[str]** | The use cases for which the source is to be registered. | [optional] 

## Example

```python
from cohesity_sdk.models.azure_source_registration_params import AzureSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSourceRegistrationParams from a JSON string
azure_source_registration_params_instance = AzureSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(AzureSourceRegistrationParams.to_json())

# convert the object into a dict
azure_source_registration_params_dict = azure_source_registration_params_instance.to_dict()
# create an instance of AzureSourceRegistrationParams from a dict
azure_source_registration_params_from_dict = AzureSourceRegistrationParams.from_dict(azure_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


