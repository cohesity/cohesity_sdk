# TenantAssignmentsResult

Result of attempted tenant assignments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **List[int]** | A list of Ids of properties assigned to the tenant. | [optional] 
**policies** | **List[str]** | A list of Ids of properties assigned to the tenant. | [optional] 
**storage_domains** | **List[int]** | A list of Ids of properties assigned to the tenant. | [optional] 
**views** | **List[int]** | A list of Ids of properties assigned to the tenant. | [optional] 
**vlans** | **List[str]** | A list of Ids of properties assigned to the tenant. | [optional] 

## Example

```python
from cohesity_sdk.models.tenant_assignments_result import TenantAssignmentsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAssignmentsResult from a JSON string
tenant_assignments_result_instance = TenantAssignmentsResult.from_json(json)
# print the JSON string representation of the object
print(TenantAssignmentsResult.to_json())

# convert the object into a dict
tenant_assignments_result_dict = tenant_assignments_result_instance.to_dict()
# create an instance of TenantAssignmentsResult from a dict
tenant_assignments_result_from_dict = TenantAssignmentsResult.from_dict(tenant_assignments_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


