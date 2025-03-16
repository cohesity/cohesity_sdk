# StandaloneClusterRegistrationParams

Specifies parameters to register HyperV failover cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 

## Example

```python
from cohesity_sdk.helios.models.standalone_cluster_registration_params import StandaloneClusterRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneClusterRegistrationParams from a JSON string
standalone_cluster_registration_params_instance = StandaloneClusterRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(StandaloneClusterRegistrationParams.to_json())

# convert the object into a dict
standalone_cluster_registration_params_dict = standalone_cluster_registration_params_instance.to_dict()
# create an instance of StandaloneClusterRegistrationParams from a dict
standalone_cluster_registration_params_from_dict = StandaloneClusterRegistrationParams.from_dict(standalone_cluster_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


