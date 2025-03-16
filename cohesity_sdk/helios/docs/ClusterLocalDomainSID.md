# ClusterLocalDomainSID

Specifies the SID of cluster local domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sid** | **str** | Specifies the SID of cluster local domain. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_local_domain_sid import ClusterLocalDomainSID

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLocalDomainSID from a JSON string
cluster_local_domain_sid_instance = ClusterLocalDomainSID.from_json(json)
# print the JSON string representation of the object
print(ClusterLocalDomainSID.to_json())

# convert the object into a dict
cluster_local_domain_sid_dict = cluster_local_domain_sid_instance.to_dict()
# create an instance of ClusterLocalDomainSID from a dict
cluster_local_domain_sid_from_dict = ClusterLocalDomainSID.from_dict(cluster_local_domain_sid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


