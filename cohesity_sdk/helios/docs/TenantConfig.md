# TenantConfig

All configurations related to tenants for an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations_enabled** | **bool** | Specifies whether organizations is enabled for the account. | 

## Example

```python
from cohesity_sdk.helios.models.tenant_config import TenantConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConfig from a JSON string
tenant_config_instance = TenantConfig.from_json(json)
# print the JSON string representation of the object
print(TenantConfig.to_json())

# convert the object into a dict
tenant_config_dict = tenant_config_instance.to_dict()
# create an instance of TenantConfig from a dict
tenant_config_from_dict = TenantConfig.from_dict(tenant_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


