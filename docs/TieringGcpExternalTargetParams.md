# TieringGcpExternalTargetParams

Specifies the parameters which are specific to GCP related External Targets of tiering purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**client_email_address** | **str** | Specifies the client email address of the external target. | 
**client_private_key** | **str** | Specifies the client private key of the external target. | [optional] 
**project_id** | **str** | Specifies the project Id of the external target. | 
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


