# KubernetesFilterParams

Specifies the parameters to in/exclude objects (e.g.: volumes). An object satisfying any of these criteria will be included by this filter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_ids** | **[[int]], none_type** | Array of Arrays of Label Ids that Specify Objects (e.g.: Persistent Volumes and Persistent Volume Claims) to Include or Exclude. Optionally specify a list of items to include in filter by listing Source Ids of Labels in this two dimensional array. Using this two dimensional array of Labels, the Cluster generates a list of items to include in the filter, which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. For example a Namespace is selected to be protected but you want to exclude all the &#39;Employees:Former&#39; items in the &#39;Location:East&#39; and &#39;Location:West&#39; but keep all the items for &#39;Employees:Former&#39; in the South which are also stored in this Namespace, by specifying the following source id array: [ [1000, 2221], [1000, 3031] ], where 1000 is the &#39;Employee:Former&#39; Label id, 2221 is the &#39;Location:East&#39; Label id and 3031 is the &#39;West&#39; Label id. The first inner array [1000, 2221] produces a list of items that are both labeled with &#39;Employees:Former&#39; and &#39;Location:East&#39; (an intersection). The second inner array [1000, 3031] produces a list of items that are both labeled with &#39;Employees:Former&#39; and &#39;Location:West&#39; (an intersection). The outer array combines the items from the two inner arrays. The list of resulting items, when combined with isExclude&#x3D;true, are then excluded from being protected this Job. | [optional] 
**objects** | **[int], none_type** | Array of objects that are to be included. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


