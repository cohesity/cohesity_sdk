# IsVaultClusterParams

Specifies the params to update whether the cluster is a vault cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_vault_cluster** | **bool** | Specifies whether the cluster is a vault cluster. | 

## Example

```python
from cohesity_sdk.cluster.models.is_vault_cluster_params import IsVaultClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of IsVaultClusterParams from a JSON string
is_vault_cluster_params_instance = IsVaultClusterParams.from_json(json)
# print the JSON string representation of the object
print(IsVaultClusterParams.to_json())

# convert the object into a dict
is_vault_cluster_params_dict = is_vault_cluster_params_instance.to_dict()
# create an instance of IsVaultClusterParams from a dict
is_vault_cluster_params_from_dict = IsVaultClusterParams.from_dict(is_vault_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


