# UdaSourceRegistrationParamsCredentials

Specifies credentials to access the Universal Data Adapter source. For e.g.: To perform backup and recovery tasks with Oracle Recovery Manager (RMAN), specify credentials for a user having 'SYSDBA' or 'SYSBACKUP' administrative privilege.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | [optional] 
**username** | **str** | Specifies the username to access target entity. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.uda_source_registration_params_credentials import UdaSourceRegistrationParamsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of UdaSourceRegistrationParamsCredentials from a JSON string
uda_source_registration_params_credentials_instance = UdaSourceRegistrationParamsCredentials.from_json(json)
# print the JSON string representation of the object
print(UdaSourceRegistrationParamsCredentials.to_json())

# convert the object into a dict
uda_source_registration_params_credentials_dict = uda_source_registration_params_credentials_instance.to_dict()
# create an instance of UdaSourceRegistrationParamsCredentials from a dict
uda_source_registration_params_credentials_from_dict = UdaSourceRegistrationParamsCredentials.from_dict(uda_source_registration_params_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


