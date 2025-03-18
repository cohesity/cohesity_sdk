# IpPool

IP pools from the vlan ip addresses, the IPs in a pool goes together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** | IP addresses. | 
**name** | **str** | Name of the IP pool. | 

## Example

```python
from cohesity_sdk.cluster.models.ip_pool import IpPool

# TODO update the JSON string below
json = "{}"
# create an instance of IpPool from a JSON string
ip_pool_instance = IpPool.from_json(json)
# print the JSON string representation of the object
print(IpPool.to_json())

# convert the object into a dict
ip_pool_dict = ip_pool_instance.to_dict()
# create an instance of IpPool from a dict
ip_pool_from_dict = IpPool.from_dict(ip_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


