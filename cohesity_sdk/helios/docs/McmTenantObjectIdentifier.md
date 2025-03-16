# McmTenantObjectIdentifier

Specifies an object protection for a given tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_hash** | **str** | Specifies the object hash of the object. | [optional] 
**object_id** | **int** | Specifies the id assigned to the object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_tenant_object_identifier import McmTenantObjectIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of McmTenantObjectIdentifier from a JSON string
mcm_tenant_object_identifier_instance = McmTenantObjectIdentifier.from_json(json)
# print the JSON string representation of the object
print(McmTenantObjectIdentifier.to_json())

# convert the object into a dict
mcm_tenant_object_identifier_dict = mcm_tenant_object_identifier_instance.to_dict()
# create an instance of McmTenantObjectIdentifier from a dict
mcm_tenant_object_identifier_from_dict = McmTenantObjectIdentifier.from_dict(mcm_tenant_object_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


