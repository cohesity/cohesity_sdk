# InitiateMultiTenantDeactivation

Specifies the response received when tenant deactivations are triggered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[InitiateTenantDeactivation]**](InitiateTenantDeactivation.md) | Specifies the tenants for whom the deactivation was requested. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.initiate_multi_tenant_deactivation import InitiateMultiTenantDeactivation

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateMultiTenantDeactivation from a JSON string
initiate_multi_tenant_deactivation_instance = InitiateMultiTenantDeactivation.from_json(json)
# print the JSON string representation of the object
print(InitiateMultiTenantDeactivation.to_json())

# convert the object into a dict
initiate_multi_tenant_deactivation_dict = initiate_multi_tenant_deactivation_instance.to_dict()
# create an instance of InitiateMultiTenantDeactivation from a dict
initiate_multi_tenant_deactivation_from_dict = InitiateMultiTenantDeactivation.from_dict(initiate_multi_tenant_deactivation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


