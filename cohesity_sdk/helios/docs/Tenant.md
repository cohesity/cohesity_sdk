# Tenant

Specifies a tenant object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_time_msecs** | **int** | Epoch time when tenant was created. | [optional] [readonly] 
**deleted_at_time_msecs** | **int** | Epoch time when tenant was last updated. | [optional] [readonly] 
**description** | **str** | Description about the tenant. | [optional] 
**id** | **str** | The tenant id. | [optional] 
**is_managed_on_helios** | **bool** | Flag to indicate if tenant is managed on helios | [optional] 
**last_updated_at_time_msecs** | **int** | Epoch time when tenant was last updated. | [optional] [readonly] 
**name** | **str** | Name of the Tenant. | [optional] 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | [optional] 
**status** | **str** | Current Status of the Tenant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print(Tenant.to_json())

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_from_dict = Tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


