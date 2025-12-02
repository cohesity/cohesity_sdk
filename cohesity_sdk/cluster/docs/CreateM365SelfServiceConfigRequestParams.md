# CreateM365SelfServiceConfigRequestParams

Specifies the request parameters to enable Self-Service for a given Microsoft365 source. The Self-Service workflow includes search & recovery of granular items within Mailbox & OneDrive workloads only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain name of the Microsoft365 Source. | 
**mailbox_params** | [**M365SelfServiceWorkloadParams**](M365SelfServiceWorkloadParams.md) |  | [optional] 
**oidc_config** | [**OIDCStandardConfiguration**](OIDCStandardConfiguration.md) |  | [optional] 
**one_drive_params** | [**M365SelfServiceWorkloadParams**](M365SelfServiceWorkloadParams.md) |  | [optional] 
**preferred_authentication_mode** | **str** | Specifies the authentication mode for Self Service workflow. If unspecified this will default to Azure AD. Otherwise Self-Service will use associated IdP OIDC Configuration. | [optional] 
**tenant_id** | **str** | Specifies the Cohesity Tenant ID for the Microsoft365 source owner. | 
**uuid** | **str** | Specifies the UUID of the Microsoft365 Source. | 

## Example

```python
from cohesity_sdk.cluster.models.create_m365_self_service_config_request_params import CreateM365SelfServiceConfigRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateM365SelfServiceConfigRequestParams from a JSON string
create_m365_self_service_config_request_params_instance = CreateM365SelfServiceConfigRequestParams.from_json(json)
# print the JSON string representation of the object
print(CreateM365SelfServiceConfigRequestParams.to_json())

# convert the object into a dict
create_m365_self_service_config_request_params_dict = create_m365_self_service_config_request_params_instance.to_dict()
# create an instance of CreateM365SelfServiceConfigRequestParams from a dict
create_m365_self_service_config_request_params_from_dict = CreateM365SelfServiceConfigRequestParams.from_dict(create_m365_self_service_config_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


