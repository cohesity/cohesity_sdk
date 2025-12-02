# InitiateTenantDeactivation

Specifies the response received when tenant deactivation is triggered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**TenantDeactivationError**](TenantDeactivationError.md) |  | [optional] 
**id** | **str** | Tenant ID. | 

## Example

```python
from cohesity_sdk.cluster.models.initiate_tenant_deactivation import InitiateTenantDeactivation

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateTenantDeactivation from a JSON string
initiate_tenant_deactivation_instance = InitiateTenantDeactivation.from_json(json)
# print the JSON string representation of the object
print(InitiateTenantDeactivation.to_json())

# convert the object into a dict
initiate_tenant_deactivation_dict = initiate_tenant_deactivation_instance.to_dict()
# create an instance of InitiateTenantDeactivation from a dict
initiate_tenant_deactivation_from_dict = InitiateTenantDeactivation.from_dict(initiate_tenant_deactivation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


