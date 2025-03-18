# GcpVpcSubnetConfig

Specifies the group of a GCP VPC and the subnet in it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet_id** | **int** | Specifies the id of the subnet. | 
**subnet_name** | **str** | Specifies the name of the subnet. | [optional] [readonly] 
**vpc_name** | **str** | Specifies the name of the vpc network. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_vpc_subnet_config import GcpVpcSubnetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GcpVpcSubnetConfig from a JSON string
gcp_vpc_subnet_config_instance = GcpVpcSubnetConfig.from_json(json)
# print the JSON string representation of the object
print(GcpVpcSubnetConfig.to_json())

# convert the object into a dict
gcp_vpc_subnet_config_dict = gcp_vpc_subnet_config_instance.to_dict()
# create an instance of GcpVpcSubnetConfig from a dict
gcp_vpc_subnet_config_from_dict = GcpVpcSubnetConfig.from_dict(gcp_vpc_subnet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


