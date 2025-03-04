# NfsSquash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **int** | GID mapped for all clients. | [optional] 
**uid** | **int** | UID mapped for all clients. | [optional] 

## Example

```python
from cohesity_sdk.models.nfs_squash import NfsSquash

# TODO update the JSON string below
json = "{}"
# create an instance of NfsSquash from a JSON string
nfs_squash_instance = NfsSquash.from_json(json)
# print the JSON string representation of the object
print(NfsSquash.to_json())

# convert the object into a dict
nfs_squash_dict = nfs_squash_instance.to_dict()
# create an instance of NfsSquash from a dict
nfs_squash_from_dict = NfsSquash.from_dict(nfs_squash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


