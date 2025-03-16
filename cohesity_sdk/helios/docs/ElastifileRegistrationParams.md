# ElastifileRegistrationParams

Specifies parameters to register an Elastifile Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | 
**endpoint** | **str** | Specifies the Hostname or IP Address Endpoint for the Elastifile Source. | 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.elastifile_registration_params import ElastifileRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ElastifileRegistrationParams from a JSON string
elastifile_registration_params_instance = ElastifileRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(ElastifileRegistrationParams.to_json())

# convert the object into a dict
elastifile_registration_params_dict = elastifile_registration_params_instance.to_dict()
# create an instance of ElastifileRegistrationParams from a dict
elastifile_registration_params_from_dict = ElastifileRegistrationParams.from_dict(elastifile_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


