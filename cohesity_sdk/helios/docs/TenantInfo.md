# TenantInfo

Description of a Tenant and it's properties.

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
from cohesity_sdk.helios.models.tenant_info import TenantInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TenantInfo from a JSON string
tenant_info_instance = TenantInfo.from_json(json)
# print the JSON string representation of the object
print(TenantInfo.to_json())

# convert the object into a dict
tenant_info_dict = tenant_info_instance.to_dict()
# create an instance of TenantInfo from a dict
tenant_info_from_dict = TenantInfo.from_dict(tenant_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


