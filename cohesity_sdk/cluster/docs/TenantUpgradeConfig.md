# TenantUpgradeConfig

Specifies the tenant config for upgrading connections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Specifies the ID of the tenant. | [optional] 
**tenant_patch_package_url** | **str** | \&quot;Specifies the patch package url to be used for patching the connections for a specific tenant. If this is provided, it will override the defaultPatchPackage URL. This URL will be used to download the package by connector. It can be http or https and must be IPv4 address or hostname (must be resolvable by connector). | [optional] 
**tenant_upgrade_package_url** | **str** | Specifies the upgrade package url to be used for upgrading the connections in the tenant. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tenant_upgrade_config import TenantUpgradeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUpgradeConfig from a JSON string
tenant_upgrade_config_instance = TenantUpgradeConfig.from_json(json)
# print the JSON string representation of the object
print(TenantUpgradeConfig.to_json())

# convert the object into a dict
tenant_upgrade_config_dict = tenant_upgrade_config_instance.to_dict()
# create an instance of TenantUpgradeConfig from a dict
tenant_upgrade_config_from_dict = TenantUpgradeConfig.from_dict(tenant_upgrade_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


