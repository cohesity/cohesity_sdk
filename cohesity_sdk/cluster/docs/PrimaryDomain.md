# PrimaryDomain

Specifies a primary domain object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Specifies the fully qualified domain name. | [optional] 
**tenant_ids** | **List[str]** | Specifies the tenants this primary domain is part of. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.primary_domain import PrimaryDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryDomain from a JSON string
primary_domain_instance = PrimaryDomain.from_json(json)
# print the JSON string representation of the object
print(PrimaryDomain.to_json())

# convert the object into a dict
primary_domain_dict = primary_domain_instance.to_dict()
# create an instance of PrimaryDomain from a dict
primary_domain_from_dict = PrimaryDomain.from_dict(primary_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


