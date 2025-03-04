# ScvmmRegistrationParams

Specifies parameters to register HyperV SCVMM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**agent_endpoint** | **str** | Specifies the agent endpoint if it is different from the source endpoint. | [optional] 
**throttling_params** | [**ThrottlingParams**](ThrottlingParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.scvmm_registration_params import ScvmmRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ScvmmRegistrationParams from a JSON string
scvmm_registration_params_instance = ScvmmRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(ScvmmRegistrationParams.to_json())

# convert the object into a dict
scvmm_registration_params_dict = scvmm_registration_params_instance.to_dict()
# create an instance of ScvmmRegistrationParams from a dict
scvmm_registration_params_from_dict = ScvmmRegistrationParams.from_dict(scvmm_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


