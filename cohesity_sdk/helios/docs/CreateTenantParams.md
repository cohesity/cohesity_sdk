# CreateTenantParams

Parameters to be specified for creating a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the tenant | [optional] 
**is_managed_on_helios** | **bool** | Flag to indicate if tenant is managed on helios | [optional] 
**name** | **str** | Name of the Tenant. | 
**tenant_id_suffix** | **str** | This suffix is used by cohesity to generate the actual tenant Id by appending the parent&#39;s tenant id to it. | 

## Example

```python
from cohesity_sdk.helios.models.create_tenant_params import CreateTenantParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantParams from a JSON string
create_tenant_params_instance = CreateTenantParams.from_json(json)
# print the JSON string representation of the object
print(CreateTenantParams.to_json())

# convert the object into a dict
create_tenant_params_dict = create_tenant_params_instance.to_dict()
# create an instance of CreateTenantParams from a dict
create_tenant_params_from_dict = CreateTenantParams.from_dict(create_tenant_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


