# ServiceNowSourceRegistrationParams

Specifies the parameters to register a ServiceNow source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_type** | **str** | Specifies the Authentication method. used by api | [optional] 
**endpoint** | **str** | Specifies the ServiceNow endpoint URL. | 
**service_now_api_key_credentials** | [**ServiceNowApiKeyCredentials**](ServiceNowApiKeyCredentials.md) |  | [optional] 
**service_now_credentials** | [**ServiceNowCredentials**](ServiceNowCredentials.md) |  | [optional] 
**service_now_o_auth2_credentials** | [**ServiceNowOAuth2Credentials**](ServiceNowOAuth2Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_now_source_registration_params import ServiceNowSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowSourceRegistrationParams from a JSON string
service_now_source_registration_params_instance = ServiceNowSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(ServiceNowSourceRegistrationParams.to_json())

# convert the object into a dict
service_now_source_registration_params_dict = service_now_source_registration_params_instance.to_dict()
# create an instance of ServiceNowSourceRegistrationParams from a dict
service_now_source_registration_params_from_dict = ServiceNowSourceRegistrationParams.from_dict(service_now_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


