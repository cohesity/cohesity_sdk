# McmTenantProfile

Specifies tenant profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[McmClusterIdentifier]**](McmClusterIdentifier.md) | Specifies the list of clusters owned by this account id. | [optional] 
**tenant_id** | **str** | Specifies the tenant id. | 
**tenant_name** | **str** | Specifies the tenant id. | [optional] [readonly] 
**tenant_type** | **str** | Specifies the type of tenant. | 

## Example

```python
from cohesity_sdk.helios.models.mcm_tenant_profile import McmTenantProfile

# TODO update the JSON string below
json = "{}"
# create an instance of McmTenantProfile from a JSON string
mcm_tenant_profile_instance = McmTenantProfile.from_json(json)
# print the JSON string representation of the object
print(McmTenantProfile.to_json())

# convert the object into a dict
mcm_tenant_profile_dict = mcm_tenant_profile_instance.to_dict()
# create an instance of McmTenantProfile from a dict
mcm_tenant_profile_from_dict = McmTenantProfile.from_dict(mcm_tenant_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


