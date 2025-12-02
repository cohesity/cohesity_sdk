# DeleteInfectedObjects

Specifies a list of infected objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_failed_infected_objects** | [**List[InfectedObject]**](InfectedObject.md) | Specifies the list of infected objects that failed deletion. | [optional] 
**delete_succeeded_infected_objects** | [**List[InfectedObject]**](InfectedObject.md) | Specifies the list of infected objects that are successfully deleted. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.delete_infected_objects import DeleteInfectedObjects

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInfectedObjects from a JSON string
delete_infected_objects_instance = DeleteInfectedObjects.from_json(json)
# print the JSON string representation of the object
print(DeleteInfectedObjects.to_json())

# convert the object into a dict
delete_infected_objects_dict = delete_infected_objects_instance.to_dict()
# create an instance of DeleteInfectedObjects from a dict
delete_infected_objects_from_dict = DeleteInfectedObjects.from_dict(delete_infected_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


