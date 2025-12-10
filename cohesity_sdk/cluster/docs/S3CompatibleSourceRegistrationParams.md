# S3CompatibleSourceRegistrationParams

Specifies the parameters to register a S3 compatible source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the access key id of the source. | 
**endpoint** | **str** | Specifies the endpoint of the source. The endpoint must be a valid IP address with the HTTPS protocol. It should not include a port or a domain name. for example: 192.168.1.1 | 
**port** | **int** | Specifies the port number for communication. | 
**secret_access_key** | **str** | Specifies the secret access key of the source. | 

## Example

```python
from cohesity_sdk.cluster.models.s3_compatible_source_registration_params import S3CompatibleSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of S3CompatibleSourceRegistrationParams from a JSON string
s3_compatible_source_registration_params_instance = S3CompatibleSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(S3CompatibleSourceRegistrationParams.to_json())

# convert the object into a dict
s3_compatible_source_registration_params_dict = s3_compatible_source_registration_params_instance.to_dict()
# create an instance of S3CompatibleSourceRegistrationParams from a dict
s3_compatible_source_registration_params_from_dict = S3CompatibleSourceRegistrationParams.from_dict(s3_compatible_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


