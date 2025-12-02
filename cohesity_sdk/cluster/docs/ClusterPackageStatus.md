# ClusterPackageStatus

Status of a package along with error message, if any.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_msg** | **str** | Error message if package is not available.  | [optional] 
**status** | **str** | Status of the package * &#x60;Available&#x60; - Package is available for use. * &#x60;DownloadFailed&#x60; - Package download has failed.  | 

## Example

```python
from cohesity_sdk.cluster.models.cluster_package_status import ClusterPackageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPackageStatus from a JSON string
cluster_package_status_instance = ClusterPackageStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterPackageStatus.to_json())

# convert the object into a dict
cluster_package_status_dict = cluster_package_status_instance.to_dict()
# create an instance of ClusterPackageStatus from a dict
cluster_package_status_from_dict = ClusterPackageStatus.from_dict(cluster_package_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


