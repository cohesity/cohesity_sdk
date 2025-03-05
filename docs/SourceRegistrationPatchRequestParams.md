# SourceRegistrationPatchRequestParams

Specifies the parameters to partially update the registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_params** | [**CassandraSourceRegistrationPatchParams**](CassandraSourceRegistrationPatchParams.md) |  | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source to be patched. Currently the only environment supported is kCassandra | 

## Example

```python
from cohesity_sdk.models.source_registration_patch_request_params import SourceRegistrationPatchRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRegistrationPatchRequestParams from a JSON string
source_registration_patch_request_params_instance = SourceRegistrationPatchRequestParams.from_json(json)
# print the JSON string representation of the object
print(SourceRegistrationPatchRequestParams.to_json())

# convert the object into a dict
source_registration_patch_request_params_dict = source_registration_patch_request_params_instance.to_dict()
# create an instance of SourceRegistrationPatchRequestParams from a dict
source_registration_patch_request_params_from_dict = SourceRegistrationPatchRequestParams.from_dict(source_registration_patch_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


