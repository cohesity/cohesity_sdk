# ActiveDirectoryTopology

Response of Active directory topology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_domains** | [**Dict[str, MemberDomain]**](MemberDomain.md) | Specifies map of domains where the key represents FQDN (fully qualified domain name) of each domain. The map contains both primary and trusted domains. | [optional] 
**primary_domains** | [**Dict[str, PrimaryDomain]**](PrimaryDomain.md) | Specifies map of primary domains where the key represents FQDN (fully qualified domain name) of each primary domain. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.active_directory_topology import ActiveDirectoryTopology

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryTopology from a JSON string
active_directory_topology_instance = ActiveDirectoryTopology.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryTopology.to_json())

# convert the object into a dict
active_directory_topology_dict = active_directory_topology_instance.to_dict()
# create an instance of ActiveDirectoryTopology from a dict
active_directory_topology_from_dict = ActiveDirectoryTopology.from_dict(active_directory_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


