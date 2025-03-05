# ClusterOperationResponseParams

Specifies cluster operation response parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | Specifies the cluster operation id. This can be used to track the progress of the operation. | [optional] 

## Example

```python
from cohesity_sdk.models.cluster_operation_response_params import ClusterOperationResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperationResponseParams from a JSON string
cluster_operation_response_params_instance = ClusterOperationResponseParams.from_json(json)
# print the JSON string representation of the object
print(ClusterOperationResponseParams.to_json())

# convert the object into a dict
cluster_operation_response_params_dict = cluster_operation_response_params_instance.to_dict()
# create an instance of ClusterOperationResponseParams from a dict
cluster_operation_response_params_from_dict = ClusterOperationResponseParams.from_dict(cluster_operation_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


