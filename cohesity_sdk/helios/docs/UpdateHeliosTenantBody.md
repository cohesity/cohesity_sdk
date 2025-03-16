# UpdateHeliosTenantBody

Request body for updating a helios tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the tenant | [optional] 
**name** | **str** | Name of the Tenant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_helios_tenant_body import UpdateHeliosTenantBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHeliosTenantBody from a JSON string
update_helios_tenant_body_instance = UpdateHeliosTenantBody.from_json(json)
# print the JSON string representation of the object
print(UpdateHeliosTenantBody.to_json())

# convert the object into a dict
update_helios_tenant_body_dict = update_helios_tenant_body_instance.to_dict()
# create an instance of UpdateHeliosTenantBody from a dict
update_helios_tenant_body_from_dict = UpdateHeliosTenantBody.from_dict(update_helios_tenant_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


