# ConfirmTenantParamsBody

Enable Helios management for a Tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the Tenant. | [optional] 
**name** | **str** | Name of the Tenant. | 

## Example

```python
from cohesity_sdk.helios.models.confirm_tenant_params_body import ConfirmTenantParamsBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmTenantParamsBody from a JSON string
confirm_tenant_params_body_instance = ConfirmTenantParamsBody.from_json(json)
# print the JSON string representation of the object
print(ConfirmTenantParamsBody.to_json())

# convert the object into a dict
confirm_tenant_params_body_dict = confirm_tenant_params_body_instance.to_dict()
# create an instance of ConfirmTenantParamsBody from a dict
confirm_tenant_params_body_from_dict = ConfirmTenantParamsBody.from_dict(confirm_tenant_params_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


