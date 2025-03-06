# CommonGcpExternalTargetParams

Specifies the common parameters which are specific to GCP related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**client_email_address** | **str** | Specifies the client email address of the external target. | 
**client_private_key** | **str** | Specifies the client private key of the external target. | [optional] 
**project_id** | **str** | Specifies the project Id of the external target. | 

## Example

```python
from cohesity_sdk.cluster.models.common_gcp_external_target_params import CommonGcpExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGcpExternalTargetParams from a JSON string
common_gcp_external_target_params_instance = CommonGcpExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonGcpExternalTargetParams.to_json())

# convert the object into a dict
common_gcp_external_target_params_dict = common_gcp_external_target_params_instance.to_dict()
# create an instance of CommonGcpExternalTargetParams from a dict
common_gcp_external_target_params_from_dict = CommonGcpExternalTargetParams.from_dict(common_gcp_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


