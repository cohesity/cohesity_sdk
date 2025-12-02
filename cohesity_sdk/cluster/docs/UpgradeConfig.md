# UpgradeConfig

Specifies the config for upgrading connections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_upgrade_configs_override** | [**List[ConnectionUpgradeConfig]**](ConnectionUpgradeConfig.md) | Specifies the upgrade config of connections to be upgraded. If the tenantUpgradeConfigs is provided, connections in the tenantUpgradeConfigs would be upgraded along with the connections in connectionUpgradeConfigs. If this is provided, it will override upgradePackageUrl and tenantUpgradeConfigsOverride for the connection. | [optional] 
**default_patch_package_url** | **str** | Specifies the patch package url for the connections. If no overrides are mentioned, this URL will be used. This URL will be used to download the package by connector. It can be http or https and must be IPv4 address or hostname (must be resolvable by the connector). | [optional] 
**default_upgrade_package_url** | **str** | Specifies the default upgrade package url for the connections unless an override is specified for a tenant or connection. All connections will be upgraded using this URL if specified. | [optional] 
**tenant_upgrade_configs_override** | [**List[TenantUpgradeConfig]**](TenantUpgradeConfig.md) | Specifies the upgrade config of tenants for which the connections would be upgraded. If this is provided, it will override defaultUpgradePackageUrl for the tenant. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.upgrade_config import UpgradeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeConfig from a JSON string
upgrade_config_instance = UpgradeConfig.from_json(json)
# print the JSON string representation of the object
print(UpgradeConfig.to_json())

# convert the object into a dict
upgrade_config_dict = upgrade_config_instance.to_dict()
# create an instance of UpgradeConfig from a dict
upgrade_config_from_dict = UpgradeConfig.from_dict(upgrade_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


