# UpdateTenantParams

Parameters to be specified for updating a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the tenant | [optional] 
**name** | **str** | Name of the Tenant. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_tenant_params import UpdateTenantParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantParams from a JSON string
update_tenant_params_instance = UpdateTenantParams.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantParams.to_json())

# convert the object into a dict
update_tenant_params_dict = update_tenant_params_instance.to_dict()
# create an instance of UpdateTenantParams from a dict
update_tenant_params_from_dict = UpdateTenantParams.from_dict(update_tenant_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


