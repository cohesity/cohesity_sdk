# TieringGcpExternalTargetParams

Specifies the parameters which are specific to GCP related External Targets of tiering purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**GCPAuthenticationMethodsParams**](GCPAuthenticationMethodsParams.md) |  | [optional] 
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**client_email_address** | **str** | Specifies the client email address of the external target. This field is being deprecated, please use authenticationMethod instead. | [optional] 
**client_private_key** | **str** | Specifies the client private key of the external target. This field is being deprecated, please use authenticationMethod instead. | [optional] 
**project_id** | **str** | Specifies the project Id of the external target. | 
**region** | **str** | Specifies the Google Cloud region where the storage bucket is located (e.g., &#39;us-central1&#39;, &#39;europe-west1&#39;). | [optional] 
**storage_class** | **str** | Specifies the GCP External Target class. | 

## Example

```python
from cohesity_sdk.cluster.models.tiering_gcp_external_target_params import TieringGcpExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of TieringGcpExternalTargetParams from a JSON string
tiering_gcp_external_target_params_instance = TieringGcpExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(TieringGcpExternalTargetParams.to_json())

# convert the object into a dict
tiering_gcp_external_target_params_dict = tiering_gcp_external_target_params_instance.to_dict()
# create an instance of TieringGcpExternalTargetParams from a dict
tiering_gcp_external_target_params_from_dict = TieringGcpExternalTargetParams.from_dict(tiering_gcp_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


