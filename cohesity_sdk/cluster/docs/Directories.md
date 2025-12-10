# Directories

Specifies the information of all the directories corresponding to the snapshot ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str** | Cookie is used for paginating results. If ReadVMDirResult is returning partial results, this field will be set. Supplying this cookie will resume listing from where this result left off. | [optional] 
**entries** | [**List[Directory]**](Directory.md) | Entries is the array of files and folders that are immediate children of the parent directory specified in the request. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.directories import Directories

# TODO update the JSON string below
json = "{}"
# create an instance of Directories from a JSON string
directories_instance = Directories.from_json(json)
# print the JSON string representation of the object
print(Directories.to_json())

# convert the object into a dict
directories_dict = directories_instance.to_dict()
# create an instance of Directories from a dict
directories_from_dict = Directories.from_dict(directories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


