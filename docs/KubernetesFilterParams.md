# KubernetesFilterParams

Specifies the parameters to in/exclude objects (e.g.: volumes). An object satisfying any of these criteria will be included by this filter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_combination_method** | **str, none_type** | Whether to include all the labels or any of them while performing inclusion/exclusion of objects. | [optional] 
**label_vector** | [**[KubernetesLabel], none_type**](KubernetesLabel.md) | Array of Object to represent Label that Specify Objects (e.g.: Persistent Volumes and Persistent Volume Claims) to Include or Exclude.It will be a two-dimensional array, where each inner array will consist of a key and value representing labels. Using this two dimensional array of Labels, the Cluster generates a list of items to include in the filter, which are derived from intersections or the union of these labels, as decided by operation parameter. | [optional] 
**objects** | **[int], none_type** | Array of objects that are to be included. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


