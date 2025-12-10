# ApplicationCredentials

Specifies the application credentials for registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_environment** | **str** | Specifies the application environment type such as kOracle, kSQL, etc. running on the Protection Source. | 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.application_credentials import ApplicationCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentials from a JSON string
application_credentials_instance = ApplicationCredentials.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentials.to_json())

# convert the object into a dict
application_credentials_dict = application_credentials_instance.to_dict()
# create an instance of ApplicationCredentials from a dict
application_credentials_from_dict = ApplicationCredentials.from_dict(application_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


