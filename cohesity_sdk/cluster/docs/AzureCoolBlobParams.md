# AzureCoolBlobParams

Specifies the parameters which are specific to Azure related with tier type Cool Blob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Specifies the category of the external target. | 
**function_app_deployment_key** | **str** | Specifies the access key to deploy Azure function to function app | [optional] 
**function_app_name** | **str** | Specifies the name of the Azure function app, which is the host of Azure functions. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_cool_blob_params import AzureCoolBlobParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCoolBlobParams from a JSON string
azure_cool_blob_params_instance = AzureCoolBlobParams.from_json(json)
# print the JSON string representation of the object
print(AzureCoolBlobParams.to_json())

# convert the object into a dict
azure_cool_blob_params_dict = azure_cool_blob_params_instance.to_dict()
# create an instance of AzureCoolBlobParams from a dict
azure_cool_blob_params_from_dict = AzureCoolBlobParams.from_dict(azure_cool_blob_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


