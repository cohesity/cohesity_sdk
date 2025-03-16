# UpdateTenantBody

Parameters to be specified for updating a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the tenant | [optional] 
**name** | **str** | Name of the Tenant. | [optional] 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_tenant_body import UpdateTenantBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantBody from a JSON string
update_tenant_body_instance = UpdateTenantBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantBody.to_json())

# convert the object into a dict
update_tenant_body_dict = update_tenant_body_instance.to_dict()
# create an instance of UpdateTenantBody from a dict
update_tenant_body_from_dict = UpdateTenantBody.from_dict(update_tenant_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


