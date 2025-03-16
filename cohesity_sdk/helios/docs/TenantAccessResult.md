# TenantAccessResult

Specifies a List of Tenant Access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_accesses** | [**List[TenantAccess]**](TenantAccess.md) | List of available Tenant Access. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tenant_access_result import TenantAccessResult

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAccessResult from a JSON string
tenant_access_result_instance = TenantAccessResult.from_json(json)
# print the JSON string representation of the object
print(TenantAccessResult.to_json())

# convert the object into a dict
tenant_access_result_dict = tenant_access_result_instance.to_dict()
# create an instance of TenantAccessResult from a dict
tenant_access_result_from_dict = TenantAccessResult.from_dict(tenant_access_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


