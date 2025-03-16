# TenantAccess

Specifies the Tenant Access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[McmClusterIdentifier]**](McmClusterIdentifier.md) | Specifies the list of clusters accessible by this access. | 
**created_time_msecs** | **int** | Specifies the timestamp in milliseconds since the epoch when this access was created. | [optional] [readonly] 
**effective_time_msecs** | **int** | Specifies the starting timestamp in milliseconds since the epoch when this access will be able allowed. | [optional] [readonly] 
**expired_time_msecs** | **int** | Specifies the timestamp in milliseconds since the epoch when this access will no longer be allowed. | [optional] [readonly] 
**is_access_active** | **bool** | Specifies whether or not this access is currently active. | [optional] [readonly] 
**last_updated_time_msecs** | **int** | Specifies the timestamp in milliseconds since the epoch when this access was updated. | [optional] [readonly] 
**roles** | **List[str]** | Specifies a list of roles associated with this access. | 
**tenant_id** | **str** | Specifies the Tenant Id of the tenant access. | 
**tenant_name** | **str** | Name of the Tenant. | [optional] [readonly] 
**tenant_status** | **str** | Specifies the Tenant status. | [optional] [readonly] 
**tenant_type** | **str** | Specifies the type of the tenant. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.tenant_access import TenantAccess

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAccess from a JSON string
tenant_access_instance = TenantAccess.from_json(json)
# print the JSON string representation of the object
print(TenantAccess.to_json())

# convert the object into a dict
tenant_access_dict = tenant_access_instance.to_dict()
# create an instance of TenantAccess from a dict
tenant_access_from_dict = TenantAccess.from_dict(tenant_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


