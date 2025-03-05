# PhysicalClusterExpandParams

Parameters to expand physical edition cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_rack_configs** | [**List[ChassisRackConfigParams]**](ChassisRackConfigParams.md) | Chassis serial to rack id mapping configuration. | [optional] 
**node_configs** | [**List[PhysicalNodeConfigParams]**](PhysicalNodeConfigParams.md) | Configuration of the nodes. | 
**vips** | **List[str]** | Virtual IPs to add to the cluster. | [optional] 

## Example

```python
from cohesity_sdk.models.physical_cluster_expand_params import PhysicalClusterExpandParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalClusterExpandParams from a JSON string
physical_cluster_expand_params_instance = PhysicalClusterExpandParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalClusterExpandParams.to_json())

# convert the object into a dict
physical_cluster_expand_params_dict = physical_cluster_expand_params_instance.to_dict()
# create an instance of PhysicalClusterExpandParams from a dict
physical_cluster_expand_params_from_dict = PhysicalClusterExpandParams.from_dict(physical_cluster_expand_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


