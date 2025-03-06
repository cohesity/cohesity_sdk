# DatastoreParams

Specifies the datastore params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the Id of the datastore. | [optional] 
**max_concurrent_streams** | **int** | Specifies the max concurrent stream per datastore. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.datastore_params import DatastoreParams

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreParams from a JSON string
datastore_params_instance = DatastoreParams.from_json(json)
# print the JSON string representation of the object
print(DatastoreParams.to_json())

# convert the object into a dict
datastore_params_dict = datastore_params_instance.to_dict()
# create an instance of DatastoreParams from a dict
datastore_params_from_dict = DatastoreParams.from_dict(datastore_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


