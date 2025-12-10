# KubernetesAutoProtectConfig

Specifies the parameters to auto protect the source after registration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies the error message in case source registration is successful but protection job creation fails | [optional] 
**is_default_auto_protected** | **bool** | Specifies if entire source should be auto protected after registration. Default: False | 
**policy_id** | **str** | Specifies the protection policy to auto protect the source with. | 
**protection_group_id** | **str** | Specifies the protection group Id after it is successfully created | [optional] 
**storage_domain_id** | **int** | Specifies the storage domain id for the protection job | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_auto_protect_config import KubernetesAutoProtectConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAutoProtectConfig from a JSON string
kubernetes_auto_protect_config_instance = KubernetesAutoProtectConfig.from_json(json)
# print the JSON string representation of the object
print(KubernetesAutoProtectConfig.to_json())

# convert the object into a dict
kubernetes_auto_protect_config_dict = kubernetes_auto_protect_config_instance.to_dict()
# create an instance of KubernetesAutoProtectConfig from a dict
kubernetes_auto_protect_config_from_dict = KubernetesAutoProtectConfig.from_dict(kubernetes_auto_protect_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


