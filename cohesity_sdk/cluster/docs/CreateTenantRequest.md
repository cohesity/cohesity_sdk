# CreateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the tenant | [optional] 
**is_managed_on_helios** | **bool** | Flag to indicate if tenant is managed on helios | [optional] 
**name** | **str** | Name of the Tenant. | 
**tenant_id_suffix** | **str** | This suffix is used by cohesity to generate the actual tenant Id by appending the parent&#39;s tenant id to it. | 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_tenant_request import CreateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantRequest from a JSON string
create_tenant_request_instance = CreateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantRequest.to_json())

# convert the object into a dict
create_tenant_request_dict = create_tenant_request_instance.to_dict()
# create an instance of CreateTenantRequest from a dict
create_tenant_request_from_dict = CreateTenantRequest.from_dict(create_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


