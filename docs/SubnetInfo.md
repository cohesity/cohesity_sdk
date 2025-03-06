# SubnetInfo

Subnet information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | Gateway. | [optional] 
**netmask_bits** | **int** | Subnet netmask bits. | [optional] 
**subnet_ip** | **str** | Subnet IP. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.subnet_info import SubnetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetInfo from a JSON string
subnet_info_instance = SubnetInfo.from_json(json)
# print the JSON string representation of the object
print(SubnetInfo.to_json())

# convert the object into a dict
subnet_info_dict = subnet_info_instance.to_dict()
# create an instance of SubnetInfo from a dict
subnet_info_from_dict = SubnetInfo.from_dict(subnet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


