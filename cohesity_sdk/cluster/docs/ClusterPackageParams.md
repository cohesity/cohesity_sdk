# ClusterPackageParams

Cluster software package parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_date** | **str** | Release date of the package. | [optional] 
**version_name** | **str** | Name of the package version. Example: 6.3.1h_release-20210714_0fad884e | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_package_params import ClusterPackageParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPackageParams from a JSON string
cluster_package_params_instance = ClusterPackageParams.from_json(json)
# print the JSON string representation of the object
print(ClusterPackageParams.to_json())

# convert the object into a dict
cluster_package_params_dict = cluster_package_params_instance.to_dict()
# create an instance of ClusterPackageParams from a dict
cluster_package_params_from_dict = ClusterPackageParams.from_dict(cluster_package_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


