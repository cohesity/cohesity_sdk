# KubernetesFilterParams

Specifies the parameters to in/exclude objects (e.g.: volumes). An object satisfying any of these criteria will be included by this filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_combination_method** | **str** | Whether to include all the labels or any of them while performing inclusion/exclusion of objects. | [optional] 
**label_vector** | [**List[KubernetesLabel]**](KubernetesLabel.md) | Array of Object to represent Label that Specify Objects (e.g.: Persistent Volumes and Persistent Volume Claims) to Include or Exclude.It will be a two-dimensional array, where each inner array will consist of a key and value representing labels. Using this two dimensional array of Labels, the Cluster generates a list of items to include in the filter, which are derived from intersections or the union of these labels, as decided by operation parameter. | [optional] 
**objects** | **List[int]** | Array of objects that are to be included. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_filter_params import KubernetesFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesFilterParams from a JSON string
kubernetes_filter_params_instance = KubernetesFilterParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesFilterParams.to_json())

# convert the object into a dict
kubernetes_filter_params_dict = kubernetes_filter_params_instance.to_dict()
# create an instance of KubernetesFilterParams from a dict
kubernetes_filter_params_from_dict = KubernetesFilterParams.from_dict(kubernetes_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


