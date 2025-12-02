# MemberDomain

Specifies a member domain object. It contains list of immediate neighbor domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Specifies the fully qualified domain name. | [optional] 
**neighbor_info** | [**List[NeighborDomain]**](NeighborDomain.md) | Specifies list of immediate neighbor domains. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.member_domain import MemberDomain

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDomain from a JSON string
member_domain_instance = MemberDomain.from_json(json)
# print the JSON string representation of the object
print(MemberDomain.to_json())

# convert the object into a dict
member_domain_dict = member_domain_instance.to_dict()
# create an instance of MemberDomain from a dict
member_domain_from_dict = MemberDomain.from_dict(member_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


