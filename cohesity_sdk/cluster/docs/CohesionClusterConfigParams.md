# CohesionClusterConfigParams

Specifies the cohesion specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | Specifies the global unique appliance ID issued by AWS. | [optional] [readonly] 
**aws_control_plane_url** | **str** | Specifies the AWS backup control plane URL. | [optional] [readonly] 
**aws_region_id** | **str** | Specifies the AWS region to which this appliance is connected to. | [optional] [readonly] 
**aws_sqs_url** | **str** | Specifies the AWS Simple Queue Service URL from which the appliance receives the necessary command messages. | [optional] [readonly] 
**aws_storage_endpoint_url** | **str** | Specifies the AWS storage endpoint to which data will be archived. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.cohesion_cluster_config_params import CohesionClusterConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of CohesionClusterConfigParams from a JSON string
cohesion_cluster_config_params_instance = CohesionClusterConfigParams.from_json(json)
# print the JSON string representation of the object
print(CohesionClusterConfigParams.to_json())

# convert the object into a dict
cohesion_cluster_config_params_dict = cohesion_cluster_config_params_instance.to_dict()
# create an instance of CohesionClusterConfigParams from a dict
cohesion_cluster_config_params_from_dict = CohesionClusterConfigParams.from_dict(cohesion_cluster_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


