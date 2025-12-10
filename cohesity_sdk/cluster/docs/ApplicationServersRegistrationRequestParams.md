# ApplicationServersRegistrationRequestParams

Specifies the application server registration request params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_environments** | **List[str]** | Specifies the list of application environments such as kOracle, kSQL, kExchange, kAD etc. running on the Protection Source. | 
**register_applications** | **bool** | If set to true registers application servers otherwise will update application servers registration. By default it is set to false. | [optional] 
**use_persistent_agent** | **bool** | Set to true if a persistent agent is running on the host. If this is specified, then credentials would not be used to log into the host environment. | [optional] 
**app_credentials_vec** | [**List[ApplicationCredentials]**](ApplicationCredentials.md) | Specifies application specific credentials vec. | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**is_internal_encrypted** | **bool** | Set to true if credentials are encrypted by internal magneto key | [optional] 
**user_encryption_key** | **str** | If set the user has encrypted the credential with userEncryptionKey. If both isInternalEncrypted and userEncryptionKey is set, it is assumed that credentials are first encrypted using &#39;internalEncryptionKey&#39; and then encrypted using &#39;userEncryptionKey&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.application_servers_registration_request_params import ApplicationServersRegistrationRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationServersRegistrationRequestParams from a JSON string
application_servers_registration_request_params_instance = ApplicationServersRegistrationRequestParams.from_json(json)
# print the JSON string representation of the object
print(ApplicationServersRegistrationRequestParams.to_json())

# convert the object into a dict
application_servers_registration_request_params_dict = application_servers_registration_request_params_instance.to_dict()
# create an instance of ApplicationServersRegistrationRequestParams from a dict
application_servers_registration_request_params_from_dict = ApplicationServersRegistrationRequestParams.from_dict(application_servers_registration_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


