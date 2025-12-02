# UdaSourceRegistrationParams

Specifies parameters to register a Universal Data Adapter source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**UdaSourceRegistrationParamsCredentials**](UdaSourceRegistrationParamsCredentials.md) |  | [optional] 
**hosts** | **List[str]** | Specifies the IPs/hostnames for the nodes forming the Universal Data Adapter source cluster. | 
**mount_view** | **bool** | Specifies if SMB/NFS view mounting should be enabled on source. Default value is false. | [optional] 
**os_type** | **str** | Specifies the OS type for Universal Data Adapter source. | [optional] 
**script_dir** | **str** | Specifies the absolute path of scripts used to interact with the Universal Data Adapter source. | 
**source_registration_args** | **str** | Specifies custom arguments to be supplied to the source registration scripts. This field is deprecated. Use sourceRegistrationArguments instead. | [optional] 
**source_registration_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the source registration scripts. | [optional] 
**source_type** | **str** | Specifies the source type for Universal Data Adapter source. | 
**view_params** | [**UdaSourceRegistrationParamsViewParams**](UdaSourceRegistrationParamsViewParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_source_registration_params import UdaSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaSourceRegistrationParams from a JSON string
uda_source_registration_params_instance = UdaSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(UdaSourceRegistrationParams.to_json())

# convert the object into a dict
uda_source_registration_params_dict = uda_source_registration_params_instance.to_dict()
# create an instance of UdaSourceRegistrationParams from a dict
uda_source_registration_params_from_dict = UdaSourceRegistrationParams.from_dict(uda_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


