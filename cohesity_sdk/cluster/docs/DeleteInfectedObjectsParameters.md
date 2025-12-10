# DeleteInfectedObjectsParameters

Specifies the parameters to delete infected objects permanently.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infected_objects** | [**List[InfectedObject]**](InfectedObject.md) | Specifies a list of infected objects to be deleted. | 

## Example

```python
from cohesity_sdk.cluster.models.delete_infected_objects_parameters import DeleteInfectedObjectsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInfectedObjectsParameters from a JSON string
delete_infected_objects_parameters_instance = DeleteInfectedObjectsParameters.from_json(json)
# print the JSON string representation of the object
print(DeleteInfectedObjectsParameters.to_json())

# convert the object into a dict
delete_infected_objects_parameters_dict = delete_infected_objects_parameters_instance.to_dict()
# create an instance of DeleteInfectedObjectsParameters from a dict
delete_infected_objects_parameters_from_dict = DeleteInfectedObjectsParameters.from_dict(delete_infected_objects_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


