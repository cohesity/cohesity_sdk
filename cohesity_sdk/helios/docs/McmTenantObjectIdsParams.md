# McmTenantObjectIdsParams

Specifies the parameters for fetching protected objects for a given tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_hashes** | **List[str]** | Specifies a list of object hashes of objects to fetch. | 
**tenant_id** | **str** | Specifies the ID of the tenant. | 

## Example

```python
from cohesity_sdk.helios.models.mcm_tenant_object_ids_params import McmTenantObjectIdsParams

# TODO update the JSON string below
json = "{}"
# create an instance of McmTenantObjectIdsParams from a JSON string
mcm_tenant_object_ids_params_instance = McmTenantObjectIdsParams.from_json(json)
# print the JSON string representation of the object
print(McmTenantObjectIdsParams.to_json())

# convert the object into a dict
mcm_tenant_object_ids_params_dict = mcm_tenant_object_ids_params_instance.to_dict()
# create an instance of McmTenantObjectIdsParams from a dict
mcm_tenant_object_ids_params_from_dict = McmTenantObjectIdsParams.from_dict(mcm_tenant_object_ids_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


