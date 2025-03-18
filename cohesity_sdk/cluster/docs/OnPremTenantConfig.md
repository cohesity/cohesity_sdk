# OnPremTenantConfig

All configurations related to tenants for the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations_enabled** | **bool** | Wether organizations is enabled on the cluster. | 
**organizations_storage_domain_sharing_enabled** | **bool** | Wether storage domain sharing is enabled for organizations on the cluster. | 

## Example

```python
from cohesity_sdk.cluster.models.on_prem_tenant_config import OnPremTenantConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremTenantConfig from a JSON string
on_prem_tenant_config_instance = OnPremTenantConfig.from_json(json)
# print the JSON string representation of the object
print(OnPremTenantConfig.to_json())

# convert the object into a dict
on_prem_tenant_config_dict = on_prem_tenant_config_instance.to_dict()
# create an instance of OnPremTenantConfig from a dict
on_prem_tenant_config_from_dict = OnPremTenantConfig.from_dict(on_prem_tenant_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


