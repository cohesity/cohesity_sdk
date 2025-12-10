# ClusterPackageFixedIssue

List of issues fixed in a package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fixed Issue ID, typically JIRA ticket number | [optional] 
**release_note** | **str** | Issue description from release notes | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_package_fixed_issue import ClusterPackageFixedIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPackageFixedIssue from a JSON string
cluster_package_fixed_issue_instance = ClusterPackageFixedIssue.from_json(json)
# print the JSON string representation of the object
print(ClusterPackageFixedIssue.to_json())

# convert the object into a dict
cluster_package_fixed_issue_dict = cluster_package_fixed_issue_instance.to_dict()
# create an instance of ClusterPackageFixedIssue from a dict
cluster_package_fixed_issue_from_dict = ClusterPackageFixedIssue.from_dict(cluster_package_fixed_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


