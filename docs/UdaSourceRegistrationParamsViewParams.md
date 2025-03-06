# UdaSourceRegistrationParamsViewParams

Specifies optional configuration parameters for the mounted view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_dir** | **str** | This field is deprecated and its value will be ignored. It was used to specify the absolute path on the host where the Cohesity view would be mounted. This is now controlled by the agent configuration and is common for all the Universal Data Adapter sources. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_source_registration_params_view_params import UdaSourceRegistrationParamsViewParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaSourceRegistrationParamsViewParams from a JSON string
uda_source_registration_params_view_params_instance = UdaSourceRegistrationParamsViewParams.from_json(json)
# print the JSON string representation of the object
print(UdaSourceRegistrationParamsViewParams.to_json())

# convert the object into a dict
uda_source_registration_params_view_params_dict = uda_source_registration_params_view_params_instance.to_dict()
# create an instance of UdaSourceRegistrationParamsViewParams from a dict
uda_source_registration_params_view_params_from_dict = UdaSourceRegistrationParamsViewParams.from_dict(uda_source_registration_params_view_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


