# AzureSourceUnRegisterParams

Specifies the paramaters to unregister an Azure source when source was registered using Express Mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_access_token** | **str** | Specifies the graph access token for using Azure graph API. | [optional] 
**management_access_token** | **str** | Specifies the management access token for using Azure management API. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_source_un_register_params import AzureSourceUnRegisterParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSourceUnRegisterParams from a JSON string
azure_source_un_register_params_instance = AzureSourceUnRegisterParams.from_json(json)
# print the JSON string representation of the object
print(AzureSourceUnRegisterParams.to_json())

# convert the object into a dict
azure_source_un_register_params_dict = azure_source_un_register_params_instance.to_dict()
# create an instance of AzureSourceUnRegisterParams from a dict
azure_source_un_register_params_from_dict = AzureSourceUnRegisterParams.from_dict(azure_source_un_register_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


