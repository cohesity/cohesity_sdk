# HeliosTenant

Description of a Tenant and it's properties on various clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_time_msecs** | **int** | Epoch time when tenant was created. | [optional] [readonly] 
**deleted_at_time_msecs** | **int** | Epoch time when tenant was last updated. | [optional] [readonly] 
**description** | **str** | Description about the tenant. | [optional] 
**id** | **str** | The tenant id. | [optional] 
**last_updated_at_time_msecs** | **int** | Epoch time when tenant was last updated. | [optional] [readonly] 
**managed_on_helios** | **bool** | Wether managed on helios or not. | [optional] 
**name** | **str** | Name of the Tenant | [optional] 
**status** | **str** | Current Status of the Tenant. | [optional] 
**systems** | [**List[HeliosClusterTenant]**](HeliosClusterTenant.md) | Details of tenant on each system that it is living. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_tenant import HeliosTenant

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTenant from a JSON string
helios_tenant_instance = HeliosTenant.from_json(json)
# print the JSON string representation of the object
print(HeliosTenant.to_json())

# convert the object into a dict
helios_tenant_dict = helios_tenant_instance.to_dict()
# create an instance of HeliosTenant from a dict
helios_tenant_from_dict = HeliosTenant.from_dict(helios_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


