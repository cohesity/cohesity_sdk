# ClusterPackages

List of cluster software packages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | [**List[ClusterPackageParams]**](ClusterPackageParams.md) | List of cluster software packages. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_packages import ClusterPackages

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPackages from a JSON string
cluster_packages_instance = ClusterPackages.from_json(json)
# print the JSON string representation of the object
print(ClusterPackages.to_json())

# convert the object into a dict
cluster_packages_dict = cluster_packages_instance.to_dict()
# create an instance of ClusterPackages from a dict
cluster_packages_from_dict = ClusterPackages.from_dict(cluster_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


