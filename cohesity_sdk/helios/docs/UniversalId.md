# UniversalId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | The id of the cluster at which the object was created. | [optional] 
**cluster_incarnation_id** | **int** | The incarnation id of the above cluster. | [optional] 
**object_id** | **int** | The object id - this is unique within the above cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.universal_id import UniversalId

# TODO update the JSON string below
json = "{}"
# create an instance of UniversalId from a JSON string
universal_id_instance = UniversalId.from_json(json)
# print the JSON string representation of the object
print(UniversalId.to_json())

# convert the object into a dict
universal_id_dict = universal_id_instance.to_dict()
# create an instance of UniversalId from a dict
universal_id_from_dict = UniversalId.from_dict(universal_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


