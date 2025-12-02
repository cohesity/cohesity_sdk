# SourceUnRegisterRequestParams

Specifies the parameters to unregister the Protection Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_params** | [**AzureSourceUnRegisterParams**](AzureSourceUnRegisterParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.source_un_register_request_params import SourceUnRegisterRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUnRegisterRequestParams from a JSON string
source_un_register_request_params_instance = SourceUnRegisterRequestParams.from_json(json)
# print the JSON string representation of the object
print(SourceUnRegisterRequestParams.to_json())

# convert the object into a dict
source_un_register_request_params_dict = source_un_register_request_params_instance.to_dict()
# create an instance of SourceUnRegisterRequestParams from a dict
source_un_register_request_params_from_dict = SourceUnRegisterRequestParams.from_dict(source_un_register_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


