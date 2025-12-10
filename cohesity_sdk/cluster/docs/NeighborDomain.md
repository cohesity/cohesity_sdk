# NeighborDomain

Specifies an immediate neighbor domain and its relationship with the primary domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Specifies the fully qualified domain name. | [optional] 
**trust_direction** | **str** | Specifies trust direction of a domain with its neighbor | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.neighbor_domain import NeighborDomain

# TODO update the JSON string below
json = "{}"
# create an instance of NeighborDomain from a JSON string
neighbor_domain_instance = NeighborDomain.from_json(json)
# print the JSON string representation of the object
print(NeighborDomain.to_json())

# convert the object into a dict
neighbor_domain_dict = neighbor_domain_instance.to_dict()
# create an instance of NeighborDomain from a dict
neighbor_domain_from_dict = NeighborDomain.from_dict(neighbor_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


