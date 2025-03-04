# IndexingPolicy

Specifies settings for indexing files found in an Object (such as a VM) so these files can be searched and recovered. This also specifies inclusion and exclusion rules that determine the directories to index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_indexing** | **bool** | Specifies if the files found in an Object (such as a VM) should be indexed. If true (the default), files are indexed. | 
**exclude_paths** | **List[str]** | Array of Excluded Directories. Specifies a list of directories to exclude from indexing.Regular expression can also be specified to provide the directory paths. Example: /Users/&lt;wildcard&gt;/AppData | [optional] 
**include_paths** | **List[str]** | Array of Indexed Directories. Specifies a list of directories to index. Regular expression can also be specified to provide the directory paths. Example: /Users/&lt;wildcard&gt;/AppData | [optional] 

## Example

```python
from cohesity_sdk.models.indexing_policy import IndexingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of IndexingPolicy from a JSON string
indexing_policy_instance = IndexingPolicy.from_json(json)
# print the JSON string representation of the object
print(IndexingPolicy.to_json())

# convert the object into a dict
indexing_policy_dict = indexing_policy_instance.to_dict()
# create an instance of IndexingPolicy from a dict
indexing_policy_from_dict = IndexingPolicy.from_dict(indexing_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


