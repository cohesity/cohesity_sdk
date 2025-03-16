# McmTenantObjectIds

Specifies the object IDs for a given tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | [**List[McmTenantObjectIdentifier]**](McmTenantObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_tenant_object_ids import McmTenantObjectIds

# TODO update the JSON string below
json = "{}"
# create an instance of McmTenantObjectIds from a JSON string
mcm_tenant_object_ids_instance = McmTenantObjectIds.from_json(json)
# print the JSON string representation of the object
print(McmTenantObjectIds.to_json())

# convert the object into a dict
mcm_tenant_object_ids_dict = mcm_tenant_object_ids_instance.to_dict()
# create an instance of McmTenantObjectIds from a dict
mcm_tenant_object_ids_from_dict = McmTenantObjectIds.from_dict(mcm_tenant_object_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


