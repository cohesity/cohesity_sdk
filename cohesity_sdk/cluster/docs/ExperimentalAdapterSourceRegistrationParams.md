# ExperimentalAdapterSourceRegistrationParams

Specifies parameters to register an Experimental Adapter source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** | Specifies the IPs/hostnames for the nodes forming the Experimental Adapter source cluster. | [optional] 
**password** | **str** | Specifies the password for the Experimental Adapter source. | [optional] 
**username** | **str** | Specifies the username for the Experimental Adapter source. | [optional] 
**workflow_params** | **str** | Specifies the discover source workflow parameters. This is a stringified JSON representation of the parameters. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapter_source_registration_params import ExperimentalAdapterSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapterSourceRegistrationParams from a JSON string
experimental_adapter_source_registration_params_instance = ExperimentalAdapterSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapterSourceRegistrationParams.to_json())

# convert the object into a dict
experimental_adapter_source_registration_params_dict = experimental_adapter_source_registration_params_instance.to_dict()
# create an instance of ExperimentalAdapterSourceRegistrationParams from a dict
experimental_adapter_source_registration_params_from_dict = ExperimentalAdapterSourceRegistrationParams.from_dict(experimental_adapter_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


